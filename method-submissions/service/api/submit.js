import { createHash, randomUUID } from 'node:crypto';

export const DOMAINS = Object.freeze({
  ate: 'Average Treatment Effect',
  cate: 'Conditional Average Treatment Effect',
  mediation: 'Mediation',
  iv: 'Instrumental Variables',
  proximal: 'Proximal Causal Inference',
  did_sc: 'Difference-in-Differences',
  nonparametric_regression: 'Nonparametric Regression',
  quantile: 'Quantile Inference',
  semi_supervised: 'Semi-Supervised Inference',
  missing_data: 'Missing Data'
});
const ORIGIN = 'https://statsinference.github.io';
const REPOSITORY = 'Statsinference/stats-inference-arena';
const REPOSITORY_ID = 1426616721;
const API = 'https://api.github.com/repos/' + REPOSITORY;
const MARKER = '<!-- arena-direct-method-list:v1 -->';
const MAX_BODY_BYTES = 2048;
const MAX_LIST_BYTES = 700000;
const MAX_NEW_PER_DAY = 50; // Durable per-domain bound; also configure hosting rate limits.
const ownDomain = value => typeof value === 'string' && Object.hasOwn(DOMAINS, value);

export function normalizeModelURL(value) {
  if (typeof value !== 'string' || value.length > 512) return null;
  const raw = value.trim();
  if (!/^https:\/\/huggingface\.co\/[A-Za-z0-9][A-Za-z0-9_-]*\/[A-Za-z0-9][A-Za-z0-9._-]*(?:\/tree\/[A-Za-z0-9][A-Za-z0-9._-]*)?\/?$/.test(raw) || raw.includes('..')) return null;
  const owner = raw.split('/')[3].toLowerCase();
  if (['spaces','datasets','organizations','api','settings','collections','join','login'].includes(owner)) return null;
  return raw.replace(/\/$/, '');
}
export function emptyList(domain) {
  if (!ownDomain(domain)) throw new Error('Invalid domain');
  return `${MARKER}\n# ${DOMAINS[domain]} — method submissions\n\n| Hugging Face model | Received (UTC) | Receipt |\n| --- | --- | --- |\n`;
}
export function readList(text, domain) {
  if (typeof text !== 'string' || Buffer.byteLength(text) > MAX_LIST_BYTES || !text.startsWith(emptyList(domain))) throw new Error('Invalid stored list');
  const tail = text.slice(emptyList(domain).length).trim();
  if (!tail) return [];
  return tail.split('\n').map(line => {
    const m = /^\| <(https:\/\/huggingface\.co\/[^>]+)> \| (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z) \| `([0-9a-f]{32})` \|$/.exec(line);
    if (!m || normalizeModelURL(m[1]) !== m[1] || !Number.isFinite(Date.parse(m[2]))) throw new Error('Invalid stored row');
    if (receiptFor(domain, m[1]) !== m[3]) throw new Error('Invalid stored receipt');
    return {url: m[1], time: m[2], receipt: m[3]};
  });
}
const receiptFor = (domain, url) => createHash('sha256').update(domain + '\n' + url).digest('hex').slice(0, 32);
const renderList = (domain, rows) => emptyList(domain) + rows.map(r => `| <${r.url}> | ${r.time} | \`${r.receipt}\` |\n`).join('');

// Test injection is local only. There is no HTTP parameter to change credentials,
// repository, branch, file path, clock, fetch implementation or repository privacy.
export function createHandler({env = process.env, fetchImpl = globalThis.fetch, now = () => new Date(), sleep = ms => new Promise(r => setTimeout(r, ms))} = {}) {
  const requests = new Map();
  const salt = randomUUID();
  return async function handler(req, res) {
    res.setHeader('Cache-Control', 'no-store');
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.setHeader('X-Content-Type-Options', 'nosniff');
    res.setHeader('Vary', 'Origin');
    const reply = (status, body) => { res.statusCode = status; res.end(body ? JSON.stringify(body) : ''); };
    const configured = env.SUBMISSIONS_ENABLED === 'true' && Boolean(env.GITHUB_SUBMISSIONS_TOKEN);
    if (req.method === 'GET') return reply(200, {ok: true, configured});
    // CORS is a browser policy, NOT authentication. The endpoint intentionally accepts
    // anonymous submissions. Content limits, quotas and hosting rate limits restrict abuse.
    if (req.headers.origin !== ORIGIN) return reply(403, {ok: false, code: 'origin_not_allowed'});
    res.setHeader('Access-Control-Allow-Origin', ORIGIN);
    if (req.method === 'OPTIONS') {
      res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
      res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Arena-Submission');
      return reply(204);
    }
    if (req.method !== 'POST') { res.setHeader('Allow', 'GET, POST, OPTIONS'); return reply(405, {ok: false, code: 'method_not_allowed'}); }
    if (req.headers['x-arena-submission'] !== '1' || !/^application\/json(?:;|$)/i.test(req.headers['content-type'] || '')) return reply(415, {ok: false, code: 'json_required'});
    if (Number(req.headers['content-length']) > MAX_BODY_BYTES) return reply(413, {ok: false, code: 'too_large'});
    let body;
    try {
      const raw = typeof req.body === 'string' ? req.body : JSON.stringify(req.body);
      if (!raw || Buffer.byteLength(raw) > MAX_BODY_BYTES) return reply(413, {ok: false, code: 'too_large'});
      body = JSON.parse(raw);
    } catch { return reply(400, {ok: false, code: 'invalid_request'}); }
    if (!body || Array.isArray(body) || typeof body !== 'object' || Object.keys(body).some(k => !['domain','huggingface_url','website'].includes(k))) return reply(400, {ok: false, code: 'invalid_request'});
    const url = normalizeModelURL(body.huggingface_url), domain = body.domain;
    if (!url || !ownDomain(domain) || (body.website !== undefined && body.website !== '')) return reply(400, {ok: false, code: 'invalid_submission'});
    if (!configured) return reply(503, {ok: false, code: 'service_unavailable'});
    const date = now(), timestamp = date.toISOString(), ms = date.getTime();
    const remote = String(req.headers['x-real-ip'] || req.socket?.remoteAddress || 'unknown').slice(0, 256);
    const client = createHash('sha256').update(salt + remote).digest('hex');
    for (const [key, value] of requests) if (value.until <= ms) requests.delete(key);
    const budget = requests.get(client) || {count: 0, until: ms + 600000};
    if (++budget.count > 5 || (requests.size >= 10000 && !requests.has(client))) { res.setHeader('Retry-After', '600'); return reply(429, {ok: false, code: 'rate_limited'}); }
    requests.set(client, budget);
    const path = `method-submissions/received/${domain}/README.md`;
    const endpoint = API + '/contents/' + path;
    const receipt = receiptFor(domain, url);
    const headers = {'Accept': 'application/vnd.github+json', 'Authorization': 'Bearer ' + env.GITHUB_SUBMISSIONS_TOKEN, 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'statistical-inference-arena-method-intake'};
    const request = (target, options = {}) => fetchImpl(target, {headers, redirect: 'error', signal: AbortSignal.timeout(5000), ...options});
    try {
      const metadata = await request(API);
      if (!metadata.ok) return reply(503, {ok: false, code: 'storage_unavailable'});
      const repo = await metadata.json();
      if (repo.id !== REPOSITORY_ID || repo.full_name !== REPOSITORY || repo.archived || repo.disabled) return reply(503, {ok: false, code: 'storage_unavailable'});
      for (let attempt = 0; attempt < 4; attempt++) {
        const read = await request(endpoint + '?ref=main');
        let sha, rows = [];
        if (read.status !== 404) {
          if (!read.ok) return reply(503, {ok: false, code: 'storage_unavailable'});
          const file = await read.json();
          if (file.type !== 'file' || file.path !== path || file.encoding !== 'base64' || typeof file.content !== 'string' || !/^[0-9a-f]{40}$/.test(file.sha) || file.size > MAX_LIST_BYTES || file.content.length > MAX_LIST_BYTES * 1.5) throw new Error('Unexpected file');
          sha = file.sha;
          rows = readList(Buffer.from(file.content, 'base64').toString('utf8'), domain);
        }
        if (rows.some(r => r.url === url)) return reply(200, {ok: true, receipt, duplicate: true});
        if (rows.filter(r => r.time.slice(0,10) === timestamp.slice(0,10)).length >= MAX_NEW_PER_DAY) { res.setHeader('Retry-After', '3600'); return reply(429, {ok: false, code: 'rate_limited'}); }
        const content = renderList(domain, [...rows, {url, time: timestamp, receipt}]);
        if (Buffer.byteLength(content) > MAX_LIST_BYTES) return reply(503, {ok: false, code: 'storage_unavailable'});
        const payload = {message: `feat: collect ${domain} method ${receipt.slice(0,12)}`, branch: 'main', content: Buffer.from(content).toString('base64'), ...(sha ? {sha} : {})};
        const saved = await request(endpoint, {method: 'PUT', headers: {...headers, 'Content-Type': 'application/json'}, body: JSON.stringify(payload)});
        if (saved.status === 409 || saved.status === 422) { await sleep(50 * (attempt + 1)); continue; }
        if (saved.status === 429 || (saved.status === 403 && (saved.headers?.get('retry-after') || saved.headers?.get('x-ratelimit-remaining') === '0'))) return reply(429, {ok: false, code: 'rate_limited'});
        if (![200,201].includes(saved.status)) return reply(503, {ok: false, code: 'save_unconfirmed'});
        const confirmed = await saved.json();
        if (confirmed.content?.path !== path || !/^[0-9a-f]{40}$/.test(confirmed.commit?.sha || '')) return reply(502, {ok: false, code: 'save_unconfirmed'});
        return reply(201, {ok: true, receipt, duplicate: false});
      }
      return reply(503, {ok: false, code: 'save_unconfirmed'});
    } catch { return reply(503, {ok: false, code: 'save_unconfirmed'}); }
  };
}
export default createHandler();
