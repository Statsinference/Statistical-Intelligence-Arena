"""Index structured ZIPs committed to GitHub; never execute contributed code.

Usage: python -m tools.dgp_registry.github_intake --incoming incoming --output registry
No model/API key, third-party hosting, or GitHub Issues required.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path
from .catalog import build
from .domains import DOMAINS, to_domain
from .zip_reader import read_archive
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
    records=[]
    notes=[]
    seen_ids={}
    seen_hashes={}
    for source in files:
        digest=hashlib.sha256(source.read_bytes()).hexdigest()
        if digest in seen_hashes:
            notes.append(f'Duplicate identical ZIP skipped: {source.as_posix()} (same as {seen_hashes[digest]})')
            continue
        seen_hashes[digest]=source.as_posix()
        parsed, warnings=read_archive(source)
        if not parsed:
            raise ValueError(f'{source}: no structured collection.json found; cannot infer DGPs without LLM')
        notes.extend(f'{source.as_posix()}: {message}' for message in warnings)
        for record in parsed:
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
                # Different scientific information with the same ID is preserved for
                # reviewer adjudication rather than overwriting or failing every record.
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
            record['domain']=area or 'unclassified'
            record['classification_status']='zip_metadata_unverified' if area else 'needs_manual_classification'
            if record.get('review_status') != 'duplicate_conflict_needs_review':
                record['review_status']='needs_scientific_review'
            record['provenance']['submission_file']=str(source.as_posix())
            record['provenance']['submitted_zip_sha256']=digest
            record['provenance']['reviewed_original_paper']=False
            record['provenance']['submitted_by']='github_file_upload'
            if not area:
                record['warnings'].append('Unrecognized or missing family in collection.json: human classification required.')
            if area=='proximal' and (record.get('estimand') or {}).get('name') in ('NDE','NIE','ACME'):
                record['suggested_secondary_domains']=['mediation']
            else:
                record['suggested_secondary_domains']=[]
            records.append(record)
    exported=export_generators(records,output,notes)
    result=build(records,output,notes)
    print(f'StatsArena: exported {exported} generator.py source file(s) without execution.')
    paper_count=len({(r.get('paper') or {}).get('doi') or (r.get('paper') or {}).get('citation') or r['record_id'] for r in records})
    print(f'StatsArena: {len(files)} ZIP file(s), {paper_count} paper(s), {result["mechanisms"]} DGP(s), {result["scenarios"]} scenario(s). All remain NEEDS REVIEW.')
    return {'zip_count':len(files),'papers':paper_count, **result}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--incoming',type=Path,default=Path('incoming'))
    parser.add_argument('--output',type=Path,default=Path('registry'))
    args=parser.parse_args()
    if not args.incoming.is_dir():
        parser.error(f'Incoming directory not found: {args.incoming}')
    ingest(args.incoming,args.output)

if __name__=='__main__':
    main()
