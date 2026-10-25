"""Read structured DGP contributions from ZIPs. NEVER execute submitted code."""
from __future__ import annotations
import csv
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path
from .latent_variables import latent_from_collection

MAX_FILES = 1500
MAX_UNCOMPRESSED_BYTES = 120 * 1024 * 1024
VALID_ID = re.compile(r'^[a-z0-9][a-z0-9-]{1,127}$')
DOI_RE = re.compile(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+')


def filehash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_doi(raw: str | None) -> str | None:
    if not raw:
        return None
    match = DOI_RE.search(str(raw))
    return match.group().rstrip('.,;)').lower() if match else None


def safe_zip(z: zipfile.ZipFile):
    members = z.infolist()
    if len(members) > MAX_FILES:
        raise ValueError(f'Archive exceeds maximum {MAX_FILES} files')
    if sum(i.file_size for i in members) > MAX_UNCOMPRESSED_BYTES:
        raise ValueError('Archive exceeds uncompressed size cap')
    for i in members:
        p = i.filename.replace('\\', '/')
        if p.startswith('/') or '..' in p.split('/') or '\x00' in p or (':' in p.split('/')[0]):
            raise ValueError('Unsafe ZIP entry: ' + p)
        if (i.external_attr >> 16) & 0o170000 == 0o120000:
            raise ValueError('Symlinks not allowed in ZIP')


def read_json(z, path, default=None):
    try:
        return json.loads(z.read(path).decode('utf-8-sig'))
    except KeyError:
        return default


def display_estimand(estimand):
    desc=str(estimand.get('definition') or '').strip()
    match=re.match(r'^(ATE|ATT|ETT|NDE|NIE|CATE|LATE|ACME|NATE)\b\s*=',desc,re.I)
    return match.group(1).upper() if match else estimand.get('symbol')


def from_collection(z, prefix, source_name, archive_sha):
    collection = read_json(z, prefix+'collection.json')
    if not isinstance(collection, dict):
        raise ValueError('Invalid collection.json under ' + prefix)
    rid = collection.get('contribution_id')
    if not isinstance(rid, str) or not VALID_ID.fullmatch(rid):
        raise ValueError('Unsafe/missing contribution ID: ' + repr(rid))
    config = read_json(z, prefix+'config.json', None)
    if not isinstance(config, dict) or not isinstance(config.get('scenarios'), dict) or not config['scenarios']:
        raise ValueError('Missing or invalid config.json scenarios under ' + prefix)
    audit = read_json(z, prefix+'source_audit.json', {}) or {}
    checks = read_json(z, prefix+'checks/report.json', {}) or {}
    if isinstance(config.get('scenarios'), dict) and config['scenarios']:
        variants = config['scenarios']
    else:
        variants = {'unspecified': {}}
    try:
        raw_csv = z.read(prefix+'schema.csv').decode('utf-8-sig')
        columns = list(csv.DictReader(io.StringIO(raw_csv)))
    except KeyError:
        columns = []
    latent_variables, latent_status = latent_from_collection(collection, columns)
    source = collection.get('source') or {}
    estimand = collection.get('estimand') or {}
    if not (source.get('citation') or source.get('url')):
        raise ValueError('Missing reference citation/URL in collection.json under ' + prefix)
    if not collection.get('equations') or not isinstance(collection.get('equations'), list):
        raise ValueError('Missing generating equations in collection.json under ' + prefix)
    if not estimand.get('definition'):
        raise ValueError('Missing estimand definition under ' + prefix)
    truth = collection.get('truth') or {}
    validated = checks.get('passed') is True
    by_scenario = {}
    for result in ((checks.get('execution') or {}).get('scenario_results') or []):
        if isinstance(result, dict):
            by_scenario[result.get('scenario')] = result.get('truth') or {}
    scenarios = []
    for variant_name, parameters in variants.items():
        checked_truth = by_scenario.get(variant_name, {})
        value = checked_truth.get('value')
        if value is None and len(variants)==1:
            value = truth.get('reference_value')
        scenarios.append({
            'id': str(variant_name), 'parameters': parameters,
            'truth': {
                'status': 'reported_numeric' if isinstance(value, (int,float)) and not isinstance(value,bool) else 'needs_review',
                'value': value if isinstance(value, (int,float)) and not isinstance(value,bool) else None,
                'expression': str(estimand.get('definition', '')),
                'derivation': str(checked_truth.get('explanation') or truth.get('method') or ''),
                'evidence': [{'file': prefix+'checks/report.json', 'location':f'execution.scenario_results[{variant_name}].truth'}] if checked_truth else [{'file':prefix+'collection.json','location':'truth'}],
            }
        })
    warnings=[]
    if not columns: warnings.append('No variable schema.csv; observed/latent distinction requires review.')
    if latent_status == 'candidates_from_equations_need_review':
        warnings.append('Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.')
    elif latent_status == 'not_explicitly_specified':
        warnings.append('No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.')
    if len(variants)>1 and any(x['truth']['value'] is None for x in scenarios):
        warnings.append('Per-scenario numerical truth missing for one or more variants.')
    if not collection.get('equations'): warnings.append('No source equations in collection.json.')
    if not source.get('locator'): warnings.append('Original paper location missing.')
    return {
        'schema_version':'0.1',
        'record_id': rid, 'kind': collection.get('kind', 'unknown'),
        'domain': str(collection.get('family') or 'unclassified'),
        'english_display': collection.get('english_display') if isinstance(collection.get('english_display'), dict) else {},
        'paper': {
            'citation': source.get('citation'), 'title': source.get('title') or source.get('paper_title'),
            'doi': normalize_doi(source.get('url') or source.get('citation')),
            'source_url': source.get('url'), 'source_file_evidence': source.get('evidence', []),
            'venue':source.get('venue'), 'year':source.get('year'),
            'source_version':source.get('version'), 'source_locator':source.get('locator'),
        },
        'mechanism': {
            'name': collection.get('title'), 'title_en':collection.get('title_en'), 'family_id':collection.get('mechanism_family_id'),
            'generation_equations':collection.get('equations') or [],
            'observed_variables': columns, 'latent_variables':latent_variables, 'latent_variables_status':latent_status,
            'sampling':collection.get('sampling'),
            'assumptions':estimand.get('assumptions') or [],
            'properties':collection.get('properties') or {},
        },
        'estimand':{'name':display_estimand(estimand), 'definition':estimand.get('definition'), 'population':None},
        'scenarios':scenarios,
        'source_relation':source.get('source_relation') or 'unknown',
        'adaptations':source.get('adaptations') or [],
        'implementation':{
            'generator_available':prefix+'generator.py' in z.namelist(),
            'generator_reference':prefix+'generator.py' if prefix+'generator.py' in z.namelist() else None,
            'truth_reference':prefix+'truth.py' if prefix+'truth.py' in z.namelist() else None,
            'source_archive':source_name,
            'code_check_reported_pass':validated,
            'scientific_acceptance':False,
        },
        'evidence':[
            {'file':prefix+'collection.json','location':'source, equations, estimand, truth'},
            {'file':prefix+'config.json','location':'scenarios'},
            {'file':prefix+'source_audit.json','location':'source review'},
        ],
        'provenance':{'mode':'structured_zip', 'archive_sha256':archive_sha,
                      'collection_sha256':filehash(z.read(prefix+'collection.json')),
                      'provided_source_pdf_verified':False,
                      'source_review_status':audit.get('review_status', 'unknown')},
        'review_status':'needs_scientific_review',
        'warnings':warnings,
    }


def read_archive_bytes(blob: bytes, source_name: str):
    if len(blob) > 25 * 1024 * 1024:
        raise ValueError("ZIP exceeds 25 MiB upload limit")
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        safe_zip(z)
        prefixes=sorted(n[:-len('collection.json')] for n in z.namelist() if n == 'collection.json' or n.endswith('/collection.json'))
        if not prefixes:
            return [], ['ZIP '+source_name+' contains no collection.json; unstructured code needs manual or AI extraction. Code is not executed.']
        records=[]
        for prefix in prefixes:
            records.append(from_collection(z,prefix,source_name,filehash(blob)))
        return records, []


def read_archive(path: Path):
    return read_archive_bytes(path.read_bytes(), path.name)
