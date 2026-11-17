"""Create browsable six-area DGP draft pages from unverified records."""
from collections import Counter, defaultdict
from itertools import groupby
from html import escape
from pathlib import Path
import json
import re
from .domains import DOMAINS, to_domain
from .math_format import equation_markdown
from .title_display import display_title
from .presentation_en import english_display, sampling_display, has_cjk
from .paper_list import paper_list_tables, _domain_papers, paper_title, paper_title_with_venue, generator_link, generator_file
from .listing_metadata import venue_abbreviation, keyword_entries, keywords, keywords_text
from .target_index import load_labels, target_name, render_target_indexes, TARGET_GROUPS
from .concise_definitions import load_definitions, concise_definition, definition_note

TARGET_LABELS = load_labels()
CONCISE_DEFINITIONS = load_definitions()


def cell(v):
    """Escape Markdown tables and disable embedded HTML in model-supplied text."""
    if v is None:
        return '—'
    return str(v).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','\\|').replace('\n',' ')


def truth_pairs(rec):
    pairs=[]
    for s in rec.get('scenarios') or []:
        est = target_name(rec, TARGET_LABELS) if not s.get('estimand') or s.get('estimand') == rec.get('estimand') else 'Needs review'
        tr = s.get('truth') or {}
        val = tr.get('value') if tr.get('value') is not None else 'not reported'
        pairs.append(f"{cell(s.get('id'))}: {cell(est)} = {cell(val)}")
    return '; '.join(pairs) if pairs else 'unknown'


def concise_target(rec, limit=90):
    """Return the source-bound audited target label, or flag for review."""
    return cell(target_name(rec, TARGET_LABELS))


def display_truth_value(truth):
    """Do not substitute an unverified expression for a missing numeric value.

    The submission format sometimes stores the estimand definition in
    truth.expression. That expression is still shown separately in the detail
    page and retained verbatim in the JSON; it is not a numeric ground truth.
    """
    value = truth.get('value')
    return 'Not reported' if value is None else value


def observed_variables_display(variables):
    """Compress only explicitly present, ordered contiguous numbered names."""
    names = [str(v.get('name')) for v in variables
             if isinstance(v, dict) and v.get('name') not in (None, '')]
    out = []
    i = 0
    while i < len(names):
        match = re.fullmatch(r'(.+?)([0-9]+)', names[i])
        end = i + 1
        if match and (len(match.group(2)) == 1 or not match.group(2).startswith('0')):
            prefix, number = match.group(1), int(match.group(2))
            while end < len(names) and names[end] == prefix + str(number + end - i):
                end += 1
        if end - i >= 4:
            out.append(f'{names[i]}–{names[end - 1]} ({end - i} variables)')
        else:
            out.extend(names[i:end])
        i = end
    return ', '.join(out), names


def review_status_display(rec):
    status = rec.get('review_status')
    if status == 'duplicate_conflict_needs_review':
        return 'Duplicate conflict — review required'
    if status == 'needs_scientific_review' or not status:
        return 'Needs scientific review'
    return str(status).replace('_', ' ')


def detail(rec):
    source_rec=rec
    rec, translated=english_display(source_rec)
    paper=rec.get('paper') or {}; mech=rec.get('mechanism') or {}
    observed, observed_names = observed_variables_display(mech.get('observed_variables') or [])
    lines=[f"# {cell(display_title(rec))}",'',
        '> **Unverified extraction — scientific review required.**','',
        f"**Primary area:** {cell(DOMAINS.get(rec.get('domain'),rec.get('domain')))}",'',
        f"**Suggested cross-tags (unverified):** {cell(', '.join(rec.get('suggested_secondary_domains') or []) or 'none')}",'',
        '## Reference paper','',
        f"**Citation:** {cell(paper.get('citation'))}",'',
        f"**DOI:** {cell(paper.get('doi'))} · **Source locator:** {cell(paper.get('source_locator'))}",'',
        '## DGP / generation mechanism','',
        f"**Sampling design:** {cell(sampling_display(mech.get('sampling')))}",'',
        '**Generator source:** ' + generator_link(rec, '../generators/'), '',
        '**Keywords (source-described):** ' + cell(keywords_text(source_rec)), '',
        '**Observed variables**', '',
        cell(observed) or '—',
        '', '**Latent variables**', '',
        cell(', '.join(str((v or {}).get('name','')) for v in mech.get('latent_variables', []) if isinstance(v,dict))) or 'Not explicitly identified (review required)',
        '', '**Latent-variable identification:** ' + cell((mech.get('latent_variables_status') or 'unknown').replace('_',' ')),
        '', '**Equations / distributions (LaTeX rendering)**', '',
        '> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.', '']
    if observed != ', '.join(observed_names):
        lines[lines.index('**Latent variables**'):lines.index('**Latent variables**')] = [
            '<details>', '<summary>All observed variable names</summary>', '',
            cell(', '.join(observed_names)), '', '</details>', '']
    if translated:
        lines.extend(['**Original source equations (verbatim):** [Open raw scientific record (JSON)](./'+source_rec['record_id']+'.json).', ''])
    lines.extend(equation_markdown(mech.get('generation_equations') or [], include_source=not translated,
                                  source_entries=(source_rec.get('mechanism') or {}).get('generation_equations') or []))
    lines.extend(['','## Parameter scenarios, estimands and truth','',
                  '<table>', '<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>', '<tbody>'])
    rows = []
    for s, source_s in zip(rec.get('scenarios') or [], source_rec.get('scenarios') or []):
        name = target_name(source_rec, TARGET_LABELS) if not source_s.get('estimand') or source_s.get('estimand') == source_rec.get('estimand') else 'Needs review'
        formula = concise_definition(source_rec, source_s, CONCISE_DEFINITIONS)
        note = definition_note(source_rec, source_s, CONCISE_DEFINITIONS)
        rows.append(((name, formula, note), s.get('id'), display_truth_value(s.get('truth') or {})))
    for (name, formula, note), group_iter in groupby(rows, key=lambda row: row[0]):
        group = list(group_iter)
        for index, (_, scenario, value) in enumerate(group):
            lines.extend(['<tr>', '<td>' + escape(str(scenario if scenario is not None else '—')) + '</td>'])
            if index == 0:
                span = str(len(group))
                lines.append('<td rowspan="' + span + '">' + escape(str(name)) + '</td>')
                lines.append('<td rowspan="' + span + '">')
                # GitHub parses inline math within HTML cells only when the
                # expression is isolated by blank lines. Escape entities, but
                # keep the trusted math delimiters and TeX intact.
                lines.extend(['', escape(str(formula)), '', '</td>'])
            lines.extend(['<td>' + escape(str(value if value is not None else '—')) + '</td>', '</tr>'])
    lines.extend(['</tbody>', '</table>'])
    notes = {}
    for source_s in source_rec.get('scenarios') or []:
        note = definition_note(source_rec, source_s, CONCISE_DEFINITIONS)
        if note:
            notes.setdefault(note, []).append(str(source_s.get('id') or 'Unnamed scenario'))
    if notes:
        lines.extend(['', '**Definition notes**', ''])
        all_scenarios = [str(s.get('id') or 'Unnamed scenario') for s in source_rec.get('scenarios') or []]
        for (note, math), scenarios in notes.items():
            formula = ('$`' + math + '`$') if math else ''
            text = ' '.join(part for part in (formula, cell(note) if note else '') if part)
            label = 'All scenarios' if scenarios == all_scenarios else ', '.join(scenarios)
            lines.append('- ' + cell(label) + ': ' + text)
    originals = {}
    for source_s in source_rec.get('scenarios') or []:
        source_e = source_s.get('estimand') or source_rec.get('estimand') or {}
        definition = source_e.get('definition') or 'Not provided'
        if has_cjk(definition):
            # Preserve the unmodified source in JSON without inserting original
            # language text into an English-only presentation page. Do not use
            # the record-level translation for a distinct scenario target.
            definition = 'Original-language definition is available in the raw scientific record (JSON).'
        originals.setdefault(str(definition), []).append(str(source_s.get('id') or 'Unnamed scenario'))
    lines.extend(['', '<details>', '<summary>Submitted estimand definitions</summary>', '',
                  'Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.', ''])
    for definition, scenarios in originals.items():
        lines.extend(['**Scenario(s):** ' + cell(', '.join(scenarios)), '', cell(definition), ''])
    lines.extend(['[Open raw scientific record (JSON)](./' + source_rec['record_id'] + '.json).', '', '</details>', ''])
    submitted_target = (source_rec.get('estimand') or {}).get('name')
    if has_cjk(submitted_target):
        lines.extend(['', '**Original submitted target notation:** [See original scientific record](./' + source_rec['record_id'] + '.json).', ''])
    else:
        lines.extend(['', '**Original submitted target notation:** ' + cell(submitted_target), ''])
    missing_expressions = [(s.get('id'), (s.get('truth') or {}).get('expression'))
                           for s in rec.get('scenarios') or []
                           if (s.get('truth') or {}).get('value') is None
                           and (s.get('truth') or {}).get('expression')]
    if missing_expressions:
        lines.extend(['', '**Stored expression (meaning requires review)**', '',
                      'An expression may have been copied from the estimand definition; '
                      'it is not a verified true value.', ''])
        for scenario_id, expression in missing_expressions:
            lines.append('- ' + cell(scenario_id) + ': ' + cell(expression))
    lines.extend(['','## Identifiability assumptions',''])
    for a in mech.get('assumptions') or []:
        lines.append('- '+cell(a))
    if not mech.get('assumptions'):
        lines.append('- Unknown / not extracted')
    lines.extend(['','## Provenance and review','',
        f"**Submitted by:** {cell((rec.get('provenance') or {}).get('submitted_by'))}",'',
        f"**Mode:** {cell((rec.get('provenance') or {}).get('mode'))}",'',
        f"**Original versus adapted:** {cell(rec.get('source_relation'))}",'',
        f"**Status:** {cell(rec.get('review_status'))}",'',
        '**Adaptations from the source (submitted, unverified):**',''])
    adaptations = source_rec.get('adaptations') or []
    if isinstance(adaptations, list) and adaptations:
        for adaptation in adaptations:
            if has_cjk(adaptation):
                lines.append('- English description pending; see [original scientific record](./' + source_rec['record_id'] + '.json).')
            else:
                lines.append('- ' + cell(adaptation))
    else:
        lines.append('- None described in the submitted metadata; this does not establish exact reproduction.')
    lines.extend(['', '**Warnings:**', ''])
    lines.extend('- '+cell(w) for w in (rec.get('warnings') or []))
    if not rec.get('warnings'):
        lines.append('- Nothing automatically flagged; this does NOT equal scientific acceptance.')
    return '\n'.join(lines)+'\n'


def build(records, output_root: Path, notes=()):
    out=Path(output_root);out.mkdir(parents=True,exist_ok=True)
    drafts=out/'drafts';drafts.mkdir(exist_ok=True)
    by=out/'by-domain';by.mkdir(exist_ok=True)
    for p in (*drafts.glob('*.json'), *drafts.glob('*.md'), *by.glob('*.md')):
        p.unlink()
    buckets=defaultdict(list)
    for rec in records:
        rid=str(rec.get('record_id') or '')
        if not re.fullmatch(r'[A-Za-z0-9_-]{1,128}',rid):
            raise ValueError('Invalid record id '+repr(rid))
        (drafts/f'{rid}.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        (drafts/f'{rid}.md').write_text(detail(rec),encoding='utf-8')
        domain=to_domain(rec.get('domain')) or 'unclassified'
        buckets[domain].append(rec)
    nscen=sum(len(r.get('scenarios') or []) for r in records)
    title=['# StatsArena — DGP Registry', '',
          '> **Draft view:** all automatically extracted records still need human scientific review.', '',
          f"**{len(records)} DGP mechanisms**, **{nscen} parameter scenarios**, **{len({(r.get('paper') or {}).get('doi') or (r.get('paper') or {}).get('citation') or r['record_id'] for r in records})} reference papers**",'',
          '## Research areas','',
          '| Research area | Papers | DGP mechanisms | Open catalog |','|---|---:|---:|---|']
    summary=['# StatsArena — submission extraction (needs review)','',
             '> Domain is provisionally inferred from the ZIP family field, not scientifically verified. Reviewers may correct classification.','']
    for key,label in DOMAINS.items():
        group=buckets.get(key,[])
        title.append(f'| {cell(label)} | {len(_domain_papers(group))} | {len(group)} | [Browse](by-domain/{key}.md) |')
        page=[f'# {label}', '',
              f'**{len(group)} submitted DGP mechanism(s) · draft / unverified.**','',
              '> Standardized target names are based on submitted definitions and require scientific review. '
              'Open each DGP for scenario definitions and reported values.', '',
              '| Paper Title | DGP mechanism | Keywords | Estimand | Scenarios | Review status |',
              '|---|---|---|---|---:|---|']
        if key in TARGET_GROUPS:
            page[4:4] = [f'[Browse estimands within this area](../by-target/{key}.md)', '']
        summary.extend([f'## {label}', ''])
        if not group:
            page.append('| — | No DGPs submitted yet | — | — | 0 | — |')
            summary.append('No submissions in this area yet.\n')
        for rec in sorted(group,key=lambda r:(str((r.get('paper') or {}).get('citation','')),r['record_id'])):
            mech=rec.get('mechanism') or {};paper=rec.get('paper') or {}
            citation=paper.get('citation') or paper.get('doi') or 'Reference pending'
            one=f"| {cell(paper_title_with_venue(rec))} | [{cell(display_title(rec))}](../drafts/{rec['record_id']}.md) | {cell(keywords_text(rec))} | {concise_target(rec)} | {len(rec.get('scenarios') or [])} | {cell(review_status_display(rec))} |"
            page.append(one)
            summary.append(one)
        summary.append('')
        (by/f'{key}.md').write_text('\n'.join(page)+'\n',encoding='utf-8')
    render_target_indexes(records, out, TARGET_LABELS)
    title.extend([''] + paper_list_tables(records, draft_prefix='drafts/', domain_prefix='by-domain/', generator_prefix='generators/'))
    if buckets.get('unclassified'):
        title.extend(['', '## Needs classification', '',
                      f"[{len(buckets['unclassified'])} unclassified DGP(s)](by-domain/unclassified.md) require a reviewer."])
        page=['# Needs classification','', '> **Unverified — reviewer must assign a research area.**', '',
              '| Paper Title | DGP | Keywords | Estimand and truth | Status |','|---|---|---|---|---|']
        for rec in buckets['unclassified']:
            p=rec.get('paper') or {}; m=rec.get('mechanism') or {}
            page.append(f"| {cell(paper_title_with_venue(rec))} | [{cell(display_title(rec))}](../drafts/{rec['record_id']}.md) | {cell(keywords_text(rec))} | {truth_pairs(rec)} | Needs classification |")
        (by/'unclassified.md').write_text('\n'.join(page)+'\n',encoding='utf-8')
    if notes:
        title+=['','## Extraction notes','']+['- '+cell(n) for n in notes]
        summary+=['','## Extraction notes','']+['- '+cell(n) for n in notes]
    (out/'INDEX.md').write_text('\n'.join(title)+'\n',encoding='utf-8')
    (out/'PR_SUMMARY.md').write_text('\n'.join(summary)+'\n',encoding='utf-8')
    (out/'catalog.json').write_text(json.dumps({
        'status':'draft_needs_review',
        'paper_count':len({(r.get('paper') or {}).get('doi') or (r.get('paper') or {}).get('citation') or r['record_id'] for r in records}),
        'mechanism_count':len(records),'scenario_count':nscen,
        'domains':{key:len(buckets.get(key,[])) for key in DOMAINS},
        'records':[{'record_id':r['record_id'],'domain':r.get('domain'),'paper':(r.get('paper') or {}).get('citation'),
                    'paper_doi':(r.get('paper') or {}).get('doi'),
                    'mechanism':display_title(r),
                    'standard_target':target_name(r, TARGET_LABELS),
                    'paper_title':paper_title(r),
                    'venue_abbreviation':venue_abbreviation(r),
                    'keywords':keywords(r),
                    'keyword_evidence':keyword_entries(r),
                    'generator_file':generator_file(r),
                    'latent_variables':[(v or {}).get('name') for v in (r.get('mechanism') or {}).get('latent_variables',[]) if isinstance(v,dict)],
                    'truth_by_scenario':truth_pairs(r),
                    'status':r.get('review_status')} for r in records],
        'notes':list(notes)},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return {'mechanisms':len(records),'scenarios':nscen,'domains':len([k for k in DOMAINS if buckets.get(k)])}
