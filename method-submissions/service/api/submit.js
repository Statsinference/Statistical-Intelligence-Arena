import { randomUUID } from 'node:crypto';

const ORIGIN = 'https://statsinference.github.io';
const REPOSITORY = 'Statsinference/stats-inference-arena';
const REPOSITORY_ID = 1426616721;
const API = 'https://api.github.com/repos/' + REPOSITORY;
const LIMIT = 8192;
const DOMAINS = new Set(['ate','cate','mediation','iv','proximal','did_sc','nonparametric_regression','quantile','semi_supervised','missing_data','']);

export function normalizeModelURL(value) {
  if (typeof value !== 'string' || value.length > 1024 || /[\s\\<>\x00-\x1f\x7f]/.test(value.trim())) return null;
  try {
    const u = new URL(value.trim());
    if (u.protocol !== 'https:' || u.hostname !== 'huggingface.co' || u.port || u.username || u.password || u.search || u.hash) return null;
    const path = u.pathname.replace(/\/$/, '');
    if (!/^\/[A-Za-z0-9][A-Za-z0-9_-]*\/[A-Za-z0-9][A-Za-z0-9._-]*(?:\/tree\/[A-Za-z0-9][A-Za-z0-9._-]*)?$/.test(path)) return null;
    if (['spaces','datasets','organizations','api','settings','collections','join','login'].includes(path.split('/')[1].toLowerCase()) || path.includes('..')) return null;
    return 'https://huggingface.co' + path;
  } catch (_) { return null; }
}

// Dependencies are injected only by the local unit tests; no bypass is exposed by HTTP.
export function createHandler({env = process.env, fetchImpl = globalThis.fetch, uuid = randomUUID} = {}) {
  return async function handler(req, res) {
    res.setHeader('Cache-Control', 'no-store');
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.setHeader('X-Content-Type-Options', 'nosniff');
    res.setHeader('Vary', 'Origin');
    const reply = (code, body) => { res.statusCode = code; res.end(body ? JSON.stringify(body) : ''); };
    if (req.headers.origin !== ORIGIN) return reply(403, {ok: false, error: 'Origin not allowed'});
    res.setHeader('Access-Control-Allow-Origin', ORIGIN);
    if (req.method === 'OPTIONS') {
      res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
      res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Arena-Submission');
      return reply(204);
    }
    if (req.method !== 'POST') { res.setHeader('Allow', 'POST, OPTIONS'); return reply(405, {ok: false, error: 'Method not allowed'}); }
    if (req.headers['x-arena-submission'] !== '1' || !/^application\/json(?:;|$)/i.test(req.headers['content-type'] || '')) return reply(415, {ok: false, error: 'JSON required'});
    if (!env.GITHUB_SUBMISSIONS_TOKEN || !env.TURNSTILE_SECRET_KEY) return reply(503, {ok: false, error: 'Submissions unavailable'});
    if (Number(req.headers['content-length']) > LIMIT) return reply(413, {ok: false, error: 'Request too large'});
    let body;
    try {
      const raw = typeof req.body === 'string' ? req.body : JSON.stringify(req.body);
      if (!raw || Buffer.byteLength(raw, 'utf8') > LIMIT) return reply(413, {ok: false, error: 'Request too large'});
      body = JSON.parse(raw);
    } catch (_) { return reply(400, {ok: false, error: 'Invalid request'}); }
    if (!body || Array.isArray(body) || typeof body !== 'object' || Object.keys(body).some(k => !['huggingface_url','domain','turnstile_token','website'].includes(k))) return reply(400, {ok: false, error: 'Invalid request'});
    const modelURL = normalizeModelURL(body.huggingface_url);
    const domain = body.domain ?? '';
    if (!modelURL || !DOMAINS.has(domain) || (body.website !== undefined && body.website !== '')) return reply(400, {ok: false, error: 'Invalid model submission'});
    if (typeof body.turnstile_token !== 'string' || !body.turnstile_token || body.turnstile_token.length > 2048) return reply(400, {ok: false, error: 'Verification required'});
    // Never log request bodies, secrets, tokens or the content of private responses.
    // Never download or run the submitted model, code or URL.
    try {
      const verification = await fetchImpl('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
        method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({secret: env.TURNSTILE_SECRET_KEY, response: body.turnstile_token}),
        redirect: 'error', signal: AbortSignal.timeout(6000)
      });
      if (!verification.ok) return reply(503, {ok: false, error: 'Verification unavailable'});
      const challenge = await verification.json();
      if (challenge.success !== true || challenge.hostname !== 'statsinference.github.io' || challenge.action !== 'method_submit') return reply(403, {ok: false, error: 'Verification failed'});
      const headers = {'Accept': 'application/vnd.github+json', 'Authorization': 'Bearer ' + env.GITHUB_SUBMISSIONS_TOKEN, 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'statistical-inference-arena-method-intake'};
      // Check privacy on every request, before creating anything. Never fall back to a public repo.
      const metadata = await fetchImpl(API, {headers, redirect: 'error', signal: AbortSignal.timeout(6000)});
      if (!metadata.ok) return reply(503, {ok: false, error: 'Private inbox unavailable'});
      const repo = await metadata.json();
      if (repo.id !== REPOSITORY_ID || repo.full_name !== REPOSITORY || repo.private !== true || repo.has_issues !== true || repo.archived || repo.disabled) return reply(503, {ok: false, error: 'Private inbox unavailable'});
      const receipt = uuid();
      const modelId = new URL(modelURL).pathname.split('/').slice(1, 3).join('/');
      const issue = {
        title: '[Method submission] ' + modelId,
        body: [
          '## Method submission', '',
          'Hugging Face model: <' + modelURL + '>',
          'Research domain: `' + (domain || 'not specified') + '`',
          'Received (UTC): ' + new Date().toISOString(),
          'Receipt: `' + receipt + '`', '',
          'Unreviewed external submission. This is not a leaderboard result. No model code was downloaded or executed.'
        ].join('\n')
      };
      const created = await fetchImpl(API + '/issues', {
        method: 'POST', headers: {...headers, 'Content-Type': 'application/json'},
        body: JSON.stringify(issue), redirect: 'error', signal: AbortSignal.timeout(6000)
      });
      if (created.status === 429) return reply(429, {ok: false, error: 'Please try again later'});
      if (created.status !== 201) return reply(503, {ok: false, error: 'Could not confirm submission'});
      const saved = await created.json();
      if (!Number.isInteger(saved.number) || saved.number < 1) return reply(502, {ok: false, error: 'Could not confirm submission'});
      // Do not return issue IDs, private URLs, stored submissions or repository metadata.
      return reply(201, {ok: true, receipt});
    } catch (_) { return reply(503, {ok: false, error: 'Could not confirm submission'}); }
  };
}

export default createHandler();
