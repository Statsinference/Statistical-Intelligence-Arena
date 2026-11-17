"""Index structured ZIPs committed to GitHub; never execute contributed code.

Usage: python -m tools.dgp_registry.github_intake --incoming incoming --output registry
No model/API key, third-party hosting, or GitHub Issues required.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import copy
import shutil
import tempfile
from pathlib import Path
from .catalog import build, detail
from .domains import DOMAINS, to_domain
from .legacy_designs import legacy_design
from .intake_safety import (INPUT_ERRORS, failure, read_zip_report,
                            write_intake_report, refresh_navigation)
from .paper_list import paper_list_tables
from .generator_export import export_generators


def scientific_signature(record):
    """Compare scientific content, excluding archive path and review metadata."""
    paper = record.get('paper') or {}
    mechanism = record.get('mechanism') or {}
    scenario_payload = []
    for scenario in record.get('scenarios') or []:
        truth = scenario.get('truth') or {}
        scenario_payload.append({
            'id': scenario.get('id'),
            'parameters': scenario.get('parameters'),
            'estimand': scenario.get('estimand'),
            'true_value': truth.get('value'),
            'true_expression': truth.get('expression'),
            'true_status': truth.get('status'),
        })
    payload = {
        'paper_doi_or_citation': paper.get('doi') or paper.get('citation'),
        'mechanism': {
            'name': mechanism.get('name'),
            'family_id': mechanism.get('family_id'),
            'equations': mechanism.get('generation_equations'),
            'observed_variables': mechanism.get('observed_variables'),
            'sampling': mechanism.get('sampling'),
        },
        'domain': record.get('source_suggested_domain') or record.get('domain'),
        'estimand': record.get('estimand'),
        'scenarios': scenario_payload,
    }
    return json.dumps(payload, sort_keys=True, ensure_ascii=False, default=str)


def ingest(incoming: Path, output: Path):
    files=sorted(p for p in incoming.rglob('*') if p.is_file() and p.suffix.lower()=='.zip')
    incoming, output = Path(incoming), Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    previous = []
    previous_generators = {}
    for path in (output/'drafts').glob('*.json'):
        try:
            rec = json.loads(path.read_text(encoding='utf-8'))
            previous.append(rec)
            rid = rec.get('record_id', '')
            if re.fullmatch(r'[a-z0-9][a-z0-9-]{1,127}', rid):
                gen = output/'generators'/(rid+'.py')
                if gen.is_file():
                    previous_generators[rid] = gen.read_bytes()
        except (OSError, ValueError):
            pass
    records=[]
    notes=[]
    failures=[]
    failed_sources=set()
    stale_ids=set()
    seen_ids={}
    seen_hashes={}
    for source in files:
        parsed, warnings, errors, digest = read_zip_report(source)
        failures.extend(errors)
        if errors:
            failed_sources.add(source.as_posix())
        if digest is not None and digest in seen_hashes:
            notes.append(f'Duplicate identical ZIP skipped: {source.as_posix()} (same as {seen_hashes[digest]})')
            continue
        if digest is not None:
            seen_hashes[digest]=source.as_posix()
        notes.extend(f'{source.as_posix()}: {message}' for message in warnings)
        for record in parsed:
            # Catch data-dependent formatting failures before they reach the shared catalog.
            try:
                preview = copy.deepcopy(record)
                preview['domain'] = to_domain(preview.get('domain')) or 'unclassified'
                detail(preview)
                paper_list_tables([preview])
                scientific_signature(preview)
            except INPUT_ERRORS as error:
                failed_sources.add(source.as_posix())
                failures.append(failure(source.as_posix(), error,
                                        (record.get('record_id') or '')+' (rendering)'))
                continue
            id_=record['record_id']
            if id_ in seen_ids:
                existing = seen_ids[id_]
                if scientific_signature(existing) == scientific_signature(record):
                    existing['provenance'].setdefault('duplicate_submission_files', []).append(source.as_posix())
                    notes.append(
                        f'Equivalent DGP {id_} in {source.as_posix()} is already registered from '
                        f'{existing["provenance"]["submission_file"]}; merged duplicate source reference.'
                    )
                    continue
                existing['warnings'].append(
                    f'Conflicting submission with the same DGP ID in {source.as_posix()}; '
                    'review and reconcile before approval.'
                )
                existing['review_status'] = 'duplicate_conflict_needs_review'
                digest_suffix = hashlib.sha256(scientific_signature(record).encode('utf-8')).hexdigest()[:10]
                stem = id_[:100] + '-conflict-' + digest_suffix
                alternative = stem
                suffix = 2
                while alternative in seen_ids:
                    alternative = stem + '-' + str(suffix)
                    suffix += 1
                record['record_id'] = alternative
                record['review_status'] = 'duplicate_conflict_needs_review'
                record['warnings'].append(
                    f'DGP ID {id_} is already used by {existing["provenance"]["submission_file"]}, '
                    'but scientific content differs; kept separately for reviewer resolution.'
                )
                notes.append(
                    f'CONFLICT: DGP ID {id_} differs across archives; kept both as review drafts '
                    f'(second record: {alternative}).'
                )
                id_ = alternative
            seen_ids[id_]=record
            raw_area=record.get('domain')
            area=to_domain(raw_area)
            record['source_suggested_domain']=raw_area
            placement = legacy_design(record['record_id'], digest) if area == 'did_sc' else None
            if area == 'did_sc' and placement:
                area, classification_note = placement
                record['domain'] = area
                record['classification_status'] = 'source_bound_catalog_placement_needs_scientific_review'
                record['warnings'].append('Catalog placement: ' + classification_note)
            elif area == 'did_sc':
                area = None
                record['domain'] = 'unclassified'
                record['classification_status'] = 'needs_manual_classification'
                record['warnings'].append(
                    'Legacy combined DiD / Synthetic Control family does not match a source-bound classification; review the design before assigning it.')
            else:
                record['domain']=area or 'unclassified'
                record['classification_status']='zip_metadata_unverified' if area else 'needs_manual_classification'
            if record.get('review_status') != 'duplicate_conflict_needs_review':
                record['review_status']='needs_scientific_review'
            record['provenance']['submission_file']=str(source.as_posix())
            record['provenance']['submitted_zip_sha256']=digest
            record['provenance']['reviewed_original_paper']=False
            record['provenance']['submitted_by']='github_file_upload'
            if not area and to_domain(raw_area) != 'did_sc':
                record['warnings'].append('Unrecognized or missing family in collection.json: human classification required.')
            if area=='proximal' and (record.get('estimand') or {}).get('name') in ('NDE','NIE','ACME'):
                record['suggested_secondary_domains']=['mediation']
            else:
                record['suggested_secondary_domains']=[]
            records.append(record)
    # Retain last-valid records for broken replacements, clearly marked as stale.
    active_ids={r['record_id'] for r in records}
    for old in previous:
        rid=old.get('record_id')
        source=(old.get('provenance') or {}).get('submission_file')
        if source in failed_sources and rid not in active_ids:
            retained=copy.deepcopy(old)
            if to_domain(retained.get('domain')) == 'did_sc':
                placement = legacy_design(rid, (retained.get('provenance') or {}).get('submitted_zip_sha256'))
                retained['domain'] = placement[0] if placement else 'unclassified'
                if placement:
                    note = 'Catalog placement: ' + placement[1]
                    if note not in retained.setdefault('warnings', []):
                        retained['warnings'].append(note)
            retained['ingestion_status']='stale_last_valid'
            retained['review_status']='stale_last_valid_needs_review'
            warning='Latest source failed processing; this is the last valid record, not a validation of the latest ZIP.'
            if warning not in retained.setdefault('warnings',[]):
                retained['warnings'].append(warning)
            records.append(retained)
            active_ids.add(rid)
            stale_ids.add(rid)
    notes.extend('INPUT REJECTED: '+e['source']+': '+e['message'] for e in failures)
    # Stage all outputs before publishing. Internal failures do not erase the catalog.
    with tempfile.TemporaryDirectory(prefix='.dgp-intake-', dir=output.parent) as work:
        stage=Path(work)/'registry'
        if output.is_dir():
            shutil.copytree(output,stage)
        else:
            stage.mkdir()
        fresh=[r for r in records if r['record_id'] not in stale_ids]
        exported=export_generators(fresh,stage,notes)
        for record in records:
            rid=record['record_id']
            if rid not in stale_ids:
                continue
            raw=previous_generators.get(rid)
            impl=record.setdefault('implementation',{})
            if raw is not None:
                (stage/'generators'/(rid+'.py')).write_bytes(raw)
                impl['exported_generator_path']='generators/'+rid+'.py'
                impl['exported_generator_sha256']=hashlib.sha256(raw).hexdigest()
            else:
                impl.pop('exported_generator_path',None)
        result=build(records,stage,notes)
        report=write_intake_report(stage,failures,source_count=len(files),
                                   records=records,stale_ids=stale_ids)
        backup=Path(work)/'previous'
        if output.exists():
            output.rename(backup)
        try:
            stage.rename(output)
        except OSError:
            if backup.exists():
                backup.rename(output)
            raise
    print(f'StatsArena: exported {exported} generator.py source file(s) without execution.')
    paper_count=len({(r.get('paper') or {}).get('doi') or (r.get('paper') or {}).get('citation') or r['record_id'] for r in records})
    print(f'StatsArena: {len(files)} ZIP file(s), {paper_count} paper(s), {result["mechanisms"]} DGP(s), {result["scenarios"]} scenario(s). All remain NEEDS REVIEW.')
    if failures:
        print(f'INPUT WARNING: {len(failures)} rejected input(s); see registry/INTAKE_REPORT.md. Other valid submissions were indexed.')
    return {'zip_count':len(files),'papers':paper_count,
            'failure_count':len(failures),'stale_count':len(stale_ids), **result}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--incoming',type=Path,default=Path('incoming'))
    parser.add_argument('--output',type=Path,default=Path('registry'))
    args=parser.parse_args()
    if not args.incoming.is_dir():
        parser.error(f'Incoming directory not found: {args.incoming}')
    ingest(args.incoming,args.output)
    if args.incoming.resolve() == Path('incoming').resolve() and args.output.resolve() == Path('registry').resolve():
        refresh_navigation(Path('README.md'))

if __name__=='__main__':
    main()

