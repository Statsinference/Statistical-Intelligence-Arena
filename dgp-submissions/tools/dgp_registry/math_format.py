"""Conservative GitHub math renderer. Never execute or mathematically infer source content."""
from __future__ import annotations
import html
import json
import re

GREEK = {'α':'alpha','β':'beta','γ':'gamma','δ':'delta','ε':'varepsilon',
         'ϵ':'varepsilon','ζ':'zeta','η':'eta','θ':'theta','κ':'kappa',
         'λ':'lambda','μ':'mu','ν':'nu','ξ':'xi','π':'pi','ρ':'rho',
         'σ':'sigma','τ':'tau','φ':'phi','χ':'chi','ψ':'psi','ω':'omega',
         'Γ':'Gamma','Δ':'Delta','Θ':'Theta','Λ':'Lambda','Ξ':'Xi',
         'Π':'Pi','Σ':'Sigma','Φ':'Phi','Ψ':'Psi','Ω':'Omega'}
SCRIPTS = dict(zip('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜₓ',
                   '0123456789+-=()aehijklmnoprstx'))
SUPERS = dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵏⁿⁱ²³','0123456789+-=()kni23'))
SUB_RX = re.compile('['+''.join(map(re.escape,SCRIPTS))+']+')
SUP_RX = re.compile('['+''.join(map(re.escape,SUPERS))+']+')
GREEK_RX = re.compile('['+''.join(map(re.escape,GREEK))+r'](?:[a-z0-9]{1,3})?')
CJK = re.compile(r'[\u3400-\u9fff]')
MATHISH = re.compile(r'[=~∼<>≤≥∈∉≠≈∝∑Σ]|\b(?:Bernoulli|Poisson|Normal|Uniform|iid)\b')
MATRIX_RX = re.compile(r'\[\s*\[\s*[-+\d.eE,\s]+\]\s*(?:,\s*\[\s*[-+\d.eE,\s]+\]\s*)+\]')
DIAGNOSTIC_RX = re.compile(r'(?<!\\)_(?:\{[^{}]*\}|[A-Za-z0-9])\s*_(?:\{|[A-Za-z0-9])')


def original_equation(entry):
    if isinstance(entry,dict):
        return str(entry.get('expression') or entry.get('text') or entry.get('latex') or '').strip()
    return str(entry).strip()


def _split_legacy(raw):
    # Split on top-level semicolons, CJK periods, or a top-level comma before a
    # *new* sampling/assignment declaration. Never split commas inside Normal(0,SD=2).
    parts=[];buf=[];stack=[]
    brackets={'(':')','[':']','{':'}'}
    for i,c in enumerate(raw):
        if c in brackets: stack.append(brackets[c])
        elif stack and c==stack[-1]:stack.pop()
        if not stack and c in ';；。':
            if ''.join(buf).strip(): parts.append(''.join(buf).strip())
            buf=[]; continue
        if not stack and c in ',，' and buf:
            upcoming=raw[i+1:]
            match=re.match(r'\s*(?:[A-Za-z_α-ωΑ-Ω][A-Za-z0-9_α-ωΑ-Ω₀-₉ⱼₖᵢ]*|Σ)\s*(?:=|[~∼])',upcoming)
            # Only start a new declaration if the preceding item already has
            # a completed expression. This keeps joint lhs "delta,zeta~N" together.
            match=re.match(r'\s*(?:[A-Za-z_α-ωΑ-Ω][A-Za-z0-9_α-ωΑ-Ω₀-₉ⱼₖᵢ]*\s*[,，]\s*)*[A-Za-z_α-ωΑ-Ω][A-Za-z0-9_α-ωΑ-Ω₀-₉ⱼₖᵢ]*\s*(?:=|[~∼])', upcoming)
            before=''.join(buf).rstrip()
            if match and before.endswith((')',']','}')) and not re.match(r'\s*[ijkt]\s*=',upcoming):
                parts.append(before);buf=[];continue
        buf.append(c)
    if ''.join(buf).strip():parts.append(''.join(buf).strip())
    return parts


def _matrix(m):
    """Format numeric matrices with explicit column and row separators.

    GitHub MathJax renders bmatrix reliably only when the row structure is
    preserved as TeX, not flattened into a single text or array literal.
    """
    try:
        data=json.loads(m.group(0))
    except ValueError:
        return m.group(0)
    if not isinstance(data,list) or not data or len(data)>20 or not all(
        isinstance(row,list) and len(row)==len(data[0]) and all(
            isinstance(v,(int,float)) and not isinstance(v,bool) for v in row
        )
        for row in data
    ):
        return m.group(0)
    rows=[' & '.join(str(v) for v in row) for row in data]
    delimiter=' '+chr(92)*2+'\n'
    return r'\begin{bmatrix}'+'\n'+delimiter.join(rows)+'\n'+r'\end{bmatrix}'

def _safe_latex(latex):
    return re.sub(r'\\operatorname\*?\{([^{}]+)\}',r'\\mathrm{\1}',latex)


def _normalize_scripts(s):
    s = re.sub(r'Σ(?='+SUB_RX.pattern+r')','∑',s)
    s = SUB_RX.sub(lambda m:'_{'+''.join(SCRIPTS[c] for c in m.group())+'}',s)
    s = SUP_RX.sub(lambda m:'^{'+''.join(SUPERS[c] for c in m.group())+'}',s)
    return s.replace('ᵀ',r'^{\top}')


def plain_math_to_latex(source):
    s=str(source).strip().rstrip('。，,')
    if not s or CJK.search(s) or not MATHISH.search(s):return None
    if any(x in s for x in ('$$','\n','\r','<script','```')):return None
    if re.search(r'\\[A-Za-z]+',s):
        return _safe_latex(s)
    keep=[]
    def protect(macro):
        n=len(keep);keep.append(macro);return '@@MATH'+str(n)+'@@'
    s=MATRIX_RX.sub(lambda m:protect(_matrix(m)),s)
    # Literal curly braces (sets / source exp notation) are not TeX grouping.
    s=s.replace('{',r'\{').replace('}',r'\}')
    s=_normalize_scripts(s)
    symbols={'−':'-','–':'-','×':r'\times ','≤':r'\leq ', '≥':r'\geq ',
             '≠':r'\neq ','≈':r'\approx ','∈':r'\in ','∉':r'\notin ',
             '∝':r'\propto ','∑':r'\sum ','…':r'\ldots '}
    for a,b in symbols.items():s=s.replace(a,b)
    s=s.replace('...',r'\ldots ')
    funcs=[(r'\bN(\d+)?(?=\s*\()',lambda m:r'\mathcal{N}'+('_{'+m.group(1)+'}' if m.group(1) else '')),
           (r'\bNormal(?=\s*\()',lambda m:r'\mathcal{N}'),
           (r'\bSD(?=\s*=)',lambda m:r'\mathrm{SD}'),
           (r'\bBernoulli(?=\s*\()',lambda m:r'\mathrm{Bernoulli}'),
           (r'\bPoisson(?=\s*\()',lambda m:r'\mathrm{Poisson}'),
           (r'\bUniform(?=\s*\()',lambda m:r'\mathrm{Uniform}'),
           (r'\bexpit\b',lambda m:r'\mathrm{expit}'),
           (r'\bexp\b',lambda m:r'\exp'),
           (r'\blog\b',lambda m:r'\log'),
           (r'\bsin\b',lambda m:r'\sin'),
           (r'\bcos\b',lambda m:r'\cos'),
           (r'\bmax(?=\s*\()',lambda m:r'\max'),
           (r'\bmin(?=\s*\()',lambda m:r'\min'),
           (r'\bfloor(?=\s*\()',lambda m:r'\mathrm{floor}'),
           (r'\bE(?=\s*[\[(])',lambda m:r'\mathbb{E}')]
    for pat, repl in funcs:s=re.sub(pat,lambda m:protect(repl(m)),s)
    # ASCII names used as mathematical variables, not the letters p*i etc.
    greek_ascii={'epsilon':'varepsilon','delta':'delta','zeta':'zeta','tau':'tau',
                 'mu':'mu','lambda':'lambda','pi':'pi','rho':'rho','beta':'beta',
                 'alpha':'alpha','gamma':'gamma','theta':'theta','sigma':'sigma','xi':'xi'}
    ascii_rx=re.compile(r'(?<![A-Za-z])('+ '|'.join(greek_ascii) +r')(\d*)(?![A-Za-z])')
    def ascii_greek(m):
        val='\\'+greek_ascii[m.group(1)]
        if m.group(2):val+='_{'+m.group(2)+'}'
        return protect(val)
    s=ascii_rx.sub(ascii_greek,s)
    def greek(m):
        name=m.group(0);suffix=name[1:]
        result='\\'+GREEK[name[0]]
        if suffix: result+='_{'+suffix+'}'
        # Greek followed by uppercase Latin variable is *not* a subscript.
        if m.end()<len(s) and s[m.end()] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            result+=' '
        return protect(result)
    s=GREEK_RX.sub(greek,s)
    s=re.sub(r'(?<![A-Za-z\\])([A-Za-z])(\d+)',r'\1_{\2}',s)
    s=s.replace('~',r'\sim ').replace('∼',r'\sim ')
    if s.count('|')==1 and ('=' in s or r'\sim' in s):s=s.replace('|',r'\mid ')
    s=s.replace('*',r'\cdot ')
    s=re.sub(r'\^(\d+)(?![\d])',r'^{\1}',s)
    s=re.sub(r'@@MATH(\d+)@@',lambda m:keep[int(m.group(1))],s)
    s=re.sub(r'(\\(?:sim|in|notin|leq|geq|neq|approx|propto|sum))\s{2,}',
             lambda m:m.group(1)+' ',s)
    s=s.replace(r'\sum _{',r'\sum_{')
    # A legacy source is displayed verbatim rather than generating invalid TeX.
    if DIAGNOSTIC_RX.search(s):return None
    return _safe_latex(s.strip())


def formatted_blocks(entry):
    if isinstance(entry,dict) and entry.get('latex'):
        latex=str(entry['latex']).strip()
        if latex and '$$' not in latex and '```' not in latex:
            return [('math',_safe_latex(latex))]+([('text',str(entry['notes']))] if entry.get('notes') else [])
    blocks=[]
    for seg in _split_legacy(original_equation(entry)):
        heading=re.match(r'^(Additive|Nonadditive|Non-additive)\s*:\s*(.+)',seg,re.I)
        if heading:blocks.append(('label',heading.group(1)));seg=heading.group(2)
        # Handle i.i.d. as sampling notation rather than concatenated math letters.
        iid=re.match(r'^(.*?)\s+(?:iid|i\.i\.d\.)\s+((?:Normal|Uniform|Bernoulli|Poisson|N\d*)\s*\(.+)$',seg,re.I)
        if iid:
            head=plain_math_to_latex(iid.group(1)+'=0')
            tail=plain_math_to_latex('Q~'+iid.group(2))
            if head and tail:
                lhs=head.rsplit('=',1)[0]
                dist=tail.split(r'\sim',1)[1].strip()
                blocks.append(('math',lhs+r'\overset{\mathrm{iid}}{\sim} '+dist))
                continue
        # Standalone English/Chinese independence statements are prose.
        trailer=re.search(r',?\s*(?:mutually independent|independent of .+|independent from .+)\.?$',seg,re.I)
        if trailer:
            seg,plain=seg[:trailer.start()].rstrip(', '),trailer.group().strip(' ,.')
        else:plain=None
        # Conditional independence declarations with explicit source distribution.
        if '独立' in seg:
            mat=re.match(r'^(.*?)\s+独立\s*[~∼]\s*((?:N\d*|Normal|Poisson|Bernoulli|Uniform))\s*\(',seg)
            if mat:
                op=seg.find('(',mat.end()-1)
                depth=0
                close=None
                for k in range(op,len(seg)):
                    if seg[k]=='(': depth+=1
                    elif seg[k]==')':
                        depth-=1
                        if depth==0:
                            close=k+1;break
                if close is not None:
                    math_src=mat.group(1)+'~'+seg[mat.start(2):close]
                    converted=plain_math_to_latex(math_src)
                    if converted and r'\sim' in converted:
                        blocks.append(('math',converted.replace(r'\sim',r'\overset{\mathrm{ind.}}{\sim}',1)))
                        remaining=seg[close:].strip(' ,，')
                        if remaining: blocks.append(('text',remaining))
                        if plain: blocks.append(('text',plain))
                        continue
        tex=plain_math_to_latex(seg)
        blocks.append(('math',tex) if tex else ('text',seg))
        if plain:blocks.append(('text',plain))
    return blocks


def _align_assignments(blocks):
    if not (2<=len(blocks)<=4) or any(k!='math' for k,_ in blocks):return None
    rows=[]
    for _,latex in blocks:
        m=re.fullmatch(r'([A-Za-z](?:_\{[A-Za-z0-9]+\})?)=(.+)',latex)
        if not m:return None
        rows.append(m.group(1)+' &= '+m.group(2))
    return r'\begin{aligned}'+'\n'+(' '+r'\\'+'\n').join(rows)+'\n'+r'\end{aligned}'


def equation_markdown(entries, include_source=True):
    out=[]
    for entry in entries:
        blocks=formatted_blocks(entry)
        aligned=_align_assignments(blocks)
        if aligned:blocks=[('math',aligned)]
        for kind,expr in blocks:
            if kind=='math':out.extend(['$$',_safe_latex(expr),'$$',''])
            elif kind=='label':out.extend(['**'+html.escape(expr)+'**',''])
            else:out.extend([html.escape(expr),''])
    if not out:return ['- Unknown — source review required','']
    if include_source:
        out.extend(['<details>','<summary>Original source equations (verbatim)</summary>','',
                    '<pre>',html.escape('\n'.join(original_equation(x) for x in entries)),
                    '</pre>','','</details>',''])
    return out
