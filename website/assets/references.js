'use strict';
/* Method references are separate from evaluation reports and model backbones.
   Add a method-specific paper first; use its Hugging Face model page only when
   no paper is supplied. Never infer a public URL from a display name. */
const METHOD_REFERENCES = Object.freeze([
  {
    id: 'causalpfn', domains: ['ate', 'cate'], names: ['CausalPFN'],
    paper: {
      url: 'https://proceedings.neurips.cc/paper_files/paper/2025/hash/e3d3db07c1bfb63e1d0b998996de1d12-Abstract-Conference.html',
      title: 'CausalPFN: Amortized Causal Effect Estimation via In-Context Learning',
      citation: 'Balazadeh Meresht et al. (2025). Advances in Neural Information Processing Systems 38.'
    },
    huggingface: {
      url: 'https://huggingface.co/vdblm/causalpfn',
      title: 'vdblm/causalpfn'
    },
    verified: '2026-11-16'
  },
  {
    id: 'proximalfm', domains: ['proximal'], names: ['ProximalFM'],
    paper: {
      url: 'https://arxiv.org/abs/2610.08078v2',
      title: 'ProximalFM: Amortized Proximal Causal Inference under Hidden Confounding',
      citation: 'Muller et al. (2026). arXiv:2610.08078v2.'
    },
    verified: '2026-11-16'
  },
  {id: 'medipfn', domains: ['mediation'], names: ['MediPFN']},
  {id: 'iv-pfn-v02', domains: ['iv'], names: ['PFN', 'IV-PFN']},
  {id: 'did-directatt', domains: ['did_sc'], names: ['DirectATT S1', 'DirectATT S2', 'DirectATT']},
  {id: 'did-ps-or-dr', domains: ['did_sc'], names: ['PS/OR-DR S1', 'PS/OR-DR S2', 'PS/OR-DR']}
]);

(function () {
  const pending = 'A method-specific paper or Hugging Face model link has not been provided for this evaluated version.';
  function safeURL(value, kind) {
    if (typeof value !== 'string') return null;
    try {
      const url = new URL(value);
      if (url.protocol !== 'https:' || url.username || url.password) return null;
      if (kind === 'huggingface' && (url.hostname !== 'huggingface.co' || url.pathname.split('/').filter(Boolean).length < 2)) return null;
      return url.href;
    } catch (_) { return null; }
  }
  function primary(source) {
    if (!source) return null;
    const paperURL = safeURL(source.paper?.url, 'paper');
    if (paperURL) return {...source.paper, kind: 'paper', label: 'Paper', url: paperURL};
    const modelURL = safeURL(source.huggingface?.url, 'huggingface');
    if (modelURL) return {...source.huggingface, kind: 'huggingface', label: 'Hugging Face', url: modelURL};
    return null;
  }
  function lookup(domain, row) {
    if (!row || row.family !== 'pfn') return null;
    return METHOD_REFERENCES.find(ref => ref.domains.includes(domain) && ref.names.includes(row.method)) || null;
  }
  function externalLink(url, text, className, title) {
    const a = document.createElement('a');
    a.href = url; a.textContent = text; a.className = className;
    a.target = '_blank'; a.rel = 'noopener noreferrer';
    a.title = title; a.setAttribute('aria-label', title);
    return a;
  }
  function annotateTable() {
    const suite = current();
    if (!suite) return;
    document.querySelectorAll('#tbody tr').forEach(tr => {
      const name = tr.querySelector('.mname');
      if (!name || tr.querySelector('.method-ref-label')) return;
      const row = suite.rows.find(r => r.method === name.textContent && r.family === 'pfn');
      if (!row) return;
      const ref = primary(lookup(suite.domain, row));
      if (ref) {
        const originalName = name.textContent;
        name.replaceChildren(externalLink(ref.url, originalName, 'method-ref-name', row.method + ': ' + ref.title));
        const tag = externalLink(ref.url, ref.label + ' ↗', 'method-ref-label', row.method + ' — ' + ref.label + ': ' + ref.title);
        name.parentElement.insertBefore(tag, name.nextSibling);
      } else {
        const label = document.createElement('span');
        label.className = 'method-ref-label reference-pending';
        label.textContent = 'Reference pending'; label.title = pending;
        name.parentElement.insertBefore(label, name.nextSibling);
      }
    });
  }
  function renderNotes() {
    let panel = document.getElementById('method-references');
    if (!panel) {
      panel = document.createElement('details'); panel.id = 'method-references';
      panel.className = 'method-references';
      document.getElementById('table').append(panel);
    }
    const suite = current();
    const methodRows = suite ? rows().filter(r => r.family === 'pfn') : [];
    const unique = new Map();
    methodRows.forEach(row => { const source = lookup(suite.domain, row); const key = source?.id || row.method; if (!unique.has(key)) unique.set(key, {source, name: row.method.replace(/ S[12]$/, '')}); });
    panel.hidden = !unique.size;
    const wasOpen = panel.open;
    panel.replaceChildren(); panel.open = wasOpen;
    if (!unique.size) return;
    const summary = document.createElement('summary'); summary.textContent = 'Method references'; panel.append(summary);
    const body = document.createElement('div'); body.className = 'reference-list';
    for (const {source, name} of unique.values()) {
      const item = document.createElement('div'); item.className = 'reference-entry';
      const heading = document.createElement('strong'); heading.textContent = name; item.append(heading);
      const ref = primary(source);
      if (ref) {
        item.append(externalLink(ref.url, ref.title + ' ↗', 'reference-title', name + ' — ' + ref.label));
        const citation = document.createElement('p'); citation.textContent = ref.citation || 'Hugging Face model card — no method-specific paper supplied.'; item.append(citation);
        const modelURL = safeURL(source.huggingface?.url, 'huggingface');
        if (ref.kind === 'paper' && modelURL) item.append(externalLink(modelURL, 'Model on Hugging Face ↗', 'reference-secondary', name + ' model on Hugging Face'));
      } else {
        const note = document.createElement('p'); note.textContent = 'Public reference not yet provided.'; item.append(note);
      }
      body.append(item);
    }
    const note = document.createElement('p'); note.className = 'reference-note';
    note.textContent = 'References identify the methods, not the source of the benchmark scores. Evaluation reports are documented separately below.';
    body.append(note); panel.append(body);
  }
  // Wrap the existing render hooks so references survive filtering and sorting.
  const previousTable = renderTable;
  renderTable = function () { previousTable(); annotateTable(); };
  const previousResults = renderResults;
  renderResults = function () { previousResults(); renderNotes(); };
  // Also usable by future table-only views; reference priority is explicit.
  window.ArenaMethodReferences = Object.freeze({lookup, primary, safeURL});
  annotateTable(); renderNotes();
})();
