"""Extract latent variable metadata from structured DGP contributions.

No contributed code is executed. Explicit metadata takes precedence. The fallback
only lists candidates named in source-generating stochastic declarations; it is
not a proof that every latent variable was recovered.
"""
from __future__ import annotations
import re

_IDENTIFIER = re.compile(r"^[A-Za-zΑ-Ωα-ω][A-Za-z0-9_Α-Ωα-ω\u0303\u1d62-\u1d6a₀-₉ⱼₖᵢ]*$")
_DECL = re.compile(r"\s*(?:[~∼]|\\sim\b|\biid\b|\bjoint(?:ly)?\s+(?:normal|Gaussian)\b|独立\s*[~∼])", re.I)
_ASSIGN = re.compile(r"^\s*([A-Za-zΑ-Ωα-ω][A-Za-z0-9_Α-Ωα-ω\u0303₀-₉ⱼₖᵢ]*)\s*=")
_NOISE = re.compile(r"^(?:ε|ϵ|epsilon|eps|noise|error)", re.I)


def _text(item):
    if isinstance(item, dict):
        return str(item.get('expression') or item.get('text') or '')
    return str(item)


def _parts(expression):
    # Keep commas inside joint distributions; split only where a new stochastic
    # assignment begins (e.g., X0~N(...), U0~N(...)).
    result=[]
    for fragment in re.split(r'[；;。]', expression):
        ident=r'[A-Za-zΑ-Ωα-ω][A-Za-z0-9_Α-Ωα-ω\u0303₀-₉ⱼₖᵢ]*'
        sep = re.compile(r'[,，](?=\s*'+ident+r'(?:\s*[,，]\s*'+ident+r')*\s*[~∼])')
        state={'start':0}
        def split_if_new_declaration(m):
            prefix = fragment[state['start']:m.start()]
            # A|X,U~Bernoulli and delta,zeta~Normal are single declarations.
            if not re.search(r'[~∼]', prefix):
                return m.group()
            state['start']=m.end()
            return ';'
        new = sep.sub(split_if_new_declaration, fragment).split(';')
        result.extend(v.strip() for v in new if v.strip())
    return result


def _token(s):
    return s.strip().strip('()[] {}。，,').strip()


def _root(token):
    # Preserve tilde: X̃ is not the same variable as observed X.
    t=token.replace('\\tilde{','').strip('}') if token.startswith('\\tilde{') else token
    if '\u0303' in token: return token.rstrip('0123456789₀₁₂₃₄₅₆₇₈₉').split('_',1)[0]
    return re.sub(r'[_\d₀-₉ᵢⱼₖₗₘₙₒₚᵣₛₜₓ].*$', '', t)


def _observed(token, observed):
    obs={str(x.get('name') or '').strip() for x in observed if isinstance(x,dict)}
    if token in obs:
        return True
    rt = _root(token)
    if not rt:
        return False
    return any(_root(x)==rt for x in obs)


def _declared_names(segment):
    pos=_DECL.search(segment)
    if not pos: return []
    # Source-specific conditional observations are not intrinsically latent.
    # They may be recorded as masked columns (e.g. SA, SZ) in another sample.
    if re.search(r'\|[^~∼]*\b[A-Za-z]\s*=', segment[:pos.start()]):
        return []
    lhs=segment[:pos.start()].strip()
    # For conditionals, only the variable *left of* the condition bar is sampled.
    lhs=lhs.split('|',1)[0].strip()
    lhs=re.sub(r'\s+(?:independent|identically\s+distributed|jointly|独立)\s*$', '', lhs, flags=re.I)
    if lhs.startswith('('):
        match=re.match(r'^\(([^()]+)\)', lhs)
        if not match: return []
        names=match.group(1).split(',')
    else:
        # Leading prose may explain the model. We only accept concise symbols.
        names=lhs.split(',')
    cleaned=[_token(name) for name in names]
    return [name for name in cleaned if _IDENTIFIER.fullmatch(name)]


def latent_from_collection(collection, observed):
    """Return (latent_rows, status). No heuristic silently asserts completeness."""
    explicit=collection.get('latent_variables')
    if explicit is None and isinstance(collection.get('variables'),dict):
        explicit=collection['variables'].get('latent')
    if isinstance(explicit,list):
        out=[]
        for item in explicit:
            if isinstance(item,str):
                item={'name':item}
            if isinstance(item,dict) and isinstance(item.get('name'),str) and item['name'].strip():
                row=dict(item)
                row.setdefault('provenance','collection.json explicit latent_variables')
                out.append(row)
        return out,'explicit_structured_metadata'

    equations=collection.get('equations') or []
    seen={}
    roots=set()
    for i,item in enumerate(equations):
        line=_text(item)
        for part in _parts(line):
            for token in _declared_names(part):
                if _NOISE.match(token) or _observed(token,observed): continue
                if token not in seen:
                    seen[token]={'name':token,'role':'latent_candidate','evidence':{
                        'file':'collection.json','equation_index':i,'expression':part},
                        'provenance':'inferred_from_stochastic_declaration'}
                roots.add(_root(token))
    # Conservatively retain named unobserved intermediate states denoted with a tilde.
    # Their sampling variability comes from upstream generated variables.
    for i,item in enumerate(equations):
        for part in _parts(_text(item)):
            m=_ASSIGN.match(part)
            if m:
                name=m.group(1)
                if '\u0303' in name and name not in seen and not _observed(name,observed):
                    seen[name]={'name':name,'role':'unobserved_intermediate_candidate','evidence':{
                        'file':'collection.json','equation_index':i,'expression':part},
                        'provenance':'inferred_from_structural_assignment'}
    # A source may explicitly label a generated intermediate as latent.
    for i,item in enumerate(equations):
        if not isinstance(item,dict): continue
        label=str(item.get('label') or '')
        if not re.search(r'latent|unobserved|unmeasured|潜在|未观测',label,re.I):
            continue
        for part in _parts(_text(item)):
            m=_ASSIGN.match(part)
            if not m:continue
            name=m.group(1)
            if name not in seen and not _observed(name,observed) and not _NOISE.match(name):
                seen[name]={'name':name,'role':'latent_candidate','evidence':{
                    'file':'collection.json','equation_index':i,'expression':part},
                    'provenance':'inferred_from_explicit_latent_label'}
    # Conservative propagation: if U0 is explicitly generated, U1=f(U0,noise)
    # is also unobserved; a generic function/propensity symbol is not inferred.
    for i,item in enumerate(equations):
        for part in _parts(_text(item)):
            m=_ASSIGN.match(part)
            if not m: continue
            name=m.group(1)
            if _root(name) not in roots or _NOISE.match(name) or _observed(name,observed):
                continue
            if name not in seen:
                seen[name]={'name':name,'role':'latent_candidate','evidence':{
                    'file':'collection.json','equation_index':i,'expression':part},
                    'provenance':'inferred_from_structural_assignment'}
    return list(seen.values()),'candidates_from_equations_need_review' if seen else 'not_explicitly_specified'
