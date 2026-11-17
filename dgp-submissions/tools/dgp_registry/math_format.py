"""Presentation-only conversion of source notation; never evaluate DGP expressions.

Explicit LaTeX is kept as LaTeX. Legacy expressions are tokenized before scripts,
sets, powers and multiplication are typeset. Ambiguous notation is retained as
literal source instead of inventing a mathematical interpretation. The caller's
records are never mutated; original equations and per-model labels are retained.
"""
from __future__ import annotations
import html
import json
import re

GREEK = dict(zip(
    'αβγδεϵζηθκλμνξπρστφχψωΓΔΘΛΞΠΣΦΨΩ',
    'alpha beta gamma delta varepsilon varepsilon zeta eta theta kappa lambda mu nu xi pi rho sigma tau phi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Phi Psi Omega'.split()))
ASCII_GREEK = {v: v for v in GREEK.values()}
ASCII_GREEK.update(epsilon='varepsilon', eps='varepsilon', varphi='varphi')
SCRIPTS = dict(zip('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜₓ', '0123456789+-=()aehijklmnoprstx'))
SUPERS = dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵏⁿⁱ', '0123456789+-=()kni'))
CJK = re.compile(r'[\u3400-\u9fff]')
MATHISH = re.compile(r'[=~∼<>≤≥∈∉≠≈∝∑Σ]|\b(?:Bernoulli|Poisson|Normal|Uniform|iid)\b')
DIAGNOSTIC_RX = re.compile(r'(?<!\\)_(?:\{[^{}]*\}|[A-Za-z0-9])\s*_(?:\{|[A-Za-z0-9])')
MATRIX_RX = re.compile(r'\[\s*\[\s*[-+\d.eE,\s]+\]\s*(?:,\s*\[\s*[-+\d.eE,\s]+\]\s*)+\]')
FUNCTIONS = set('exp log ln sin cos tan tanh sinh cosh min max inf sup logit expit sqrt abs floor ceil sign logistic softplus logaddexp expm1 log1p'.split())
DISTRIBUTIONS = set('N Normal Uniform Bernoulli Poisson Binomial Beta Gamma Exponential Cauchy Logistic Laplace LogNormal lognormal TruncatedNormal Multinomial'.split())
WORDS = set(('if otherwise for where with and or at in not iid independently independent '
             'of from across individuals there is a the an as on by to only observed '
             'placeholder mutually each all no added noise continuous endpoint extensions '
             'drawn once fixed source population when then whose conditionally respectively '
             'variance scale shape rate location mean vector coordinates rows').split())
SYMBOLS = {'∼':r'\sim ', '~':r'\sim ', '≤':r'\leq ', '≥':r'\geq ', '≠':r'\neq ',
           '±':r'\pm ', '≈':r'\approx ', '∈':r'\in ', '∉':r'\notin ', '∝':r'\propto ',
           '∑':r'\sum', '∏':r'\prod', '∞':r'\infty', '×':r'\times ',
           '·':r'\cdot ', '−':'-', '–':'-', '…':r'\ldots ', '⊥':r'\perp ', '⟂':r'\perp '}


# Exact-source presentation repairs, not DGP overrides. The scalar sums in
# iv-ye-2024-genius-heteroskedastic-v1 and iv-hoshino-2024-ring-network-v1
# are also explicit sum/math.fsum calls in their unchanged generators. Matching the complete expression prevents a changed
# contribution from silently inheriting a stale, paper-specific transcription.
_REVIEWED_SUMS = {
    "A=Σ_{j}γ_{j}Z_{j}+U+(1+Σ_{j}δ_{j}Z_{j})ε_{A},",
    "Y=0.4A+Σ_{j}α_{j}Z_{j}+U+ε_{Y}.",
    "DGP1: D_{i}=1{γ_{0i}+Z_{i}+Σ_{j∈Nᵢ}Z_{j} ≥ 0},",
    "Y_{i}=β_{0i}+β_{1i}D_{i}+β_{2i}Σ_{j∈Nᵢ}D_{j}.",
    "θ=Σ_{i}β_{1i}w_{i} / Σ_{i}w_{i}.",
}


# Exact legacy source strings from the binary IV simulation. The source
# declares c, a, n and q separately; adjacent cq is their product, not one
# identifier. Exact matching makes this a display repair, not a DGP change.
_REVIEWED_IV_PRODUCTS = {
    "c=φ_{1}, a=(1−c)φ_{2}, n=(1−c)(1−φ_{2}).":
        r"c=\phi_{1},\quad a=(1-c)\phi_{2},\quad n=(1-c)(1-\phi_{2})",
    "p_{0}=(n(1−φ_{3})+c(1−q_{0}), nφ_{3}+cq_{0}, a(1−φ_{4}), aφ_{4}),":
        r"p_{0}=(n(1-\phi_{3})+c(1-q_{0}),\ n\phi_{3}+c q_{0},\ a(1-\phi_{4}),\ a\phi_{4})",
    "p_{1}=(n(1−φ_{3}), nφ_{3}, a(1−φ_{4})+c(1−q_{1}), aφ_{4}+cq_{1}).":
        r"p_{1}=(n(1-\phi_{3}),\ n\phi_{3},\ a(1-\phi_{4})+c(1-q_{1}),\ a\phi_{4}+c q_{1})",
}


class UncertainNotation(ValueError):
    """The source is not sufficiently explicit for an automatic math rewrite."""


def original_equation(entry):
    if isinstance(entry, dict):
        return str(entry.get('expression') or entry.get('text') or entry.get('latex') or '')
    return str(entry)


def _unwrap(value):
    s = str(value).strip()
    for _ in range(3):
        for left, right in [('$$','$$'), (r'\[',r'\]'), (r'\(',r'\)'), ('$','$'), ('`','`')]:
            if s.startswith(left) and s.endswith(right) and len(s) >= len(left)+len(right):
                s = s[len(left):-len(right)].strip()
                break
        else:
            break
    return s


def _escape_hashes(latex):
    """Escape literal hashes and cardinality set delimiters, never macros."""
    if '#' not in latex:
        return latex
    if re.search(r'\\(?:def|gdef|edef|xdef|newcommand|renewcommand|providecommand|DeclareMathOperator|verb)\b', latex):
        return None
    result, stack, i = [], [], 0
    while i < len(latex):
        c = latex[i]
        if c == '\\':
            result.append(latex[i:i+2])
            i += 2
            continue
        if c == '#':
            result.append(r'\#')
            if latex[i+1:i+2] == '{':
                result.append(r'\{')
                stack.append(True)
                i += 2
                continue
        elif c == '{':
            stack.append(False)
        elif c == '}':
            if not stack:
                return None
            if stack.pop():
                result.append(r'\}')
                i += 1
                continue
        result.append(c) if c != '#' else None
        i += 1
    return None if stack else ''.join(result)


def _safe_latex(latex):
    # Unescaped hashes cannot be rendered as ordinary math; repair literal
    # cardinality notation, but leave macro definitions as source text.
    latex = _escape_hashes(_unwrap(latex))
    if latex is None:
        return None
    # Distribution names historically use mathrm in this repository. Do not
    # rewrite starred operators: their limit placement carries meaning.
    return re.sub(r'\\operatorname\{(Bernoulli|Poisson|Uniform|Normal|expit|Exp|sinc)\}',
                  lambda m: r'\mathrm{' + m[1] + '}', latex)

def _balanced(s):
    depth = 0
    for m in re.finditer(r'\\.|[{}]', s, re.S):
        c = m[0]
        if c == '{': depth += 1
        if c == '}': depth -= 1
        if depth < 0: return False
    return depth == 0


def _split_legacy(raw):
    parts, buf, stack = [], [], []
    for i, c in enumerate(raw):
        if c in '([{': stack.append({'(':')','[':']','{':'}'}[c])
        elif stack and (c == stack[-1] or (c in ')]' and stack[-1] in ')]')): stack.pop()
        split = not stack and c in ';；。'
        if not stack and c in ',，' and buf:
            upcoming = raw[i+1:]
            match = re.match(r'\s*(?:[A-Za-z_α-ωΑ-Ω][A-Za-z0-9_α-ωΑ-Ω₀-₉ⱼₖᵢ]*\s*[,，]\s*)*[A-Za-z_α-ωΑ-Ω][A-Za-z0-9_α-ωΑ-Ω₀-₉ⱼₖᵢ]*\s*(?:=|[~∼])', upcoming)
            split = bool(match and ''.join(buf).rstrip().endswith((')',']','}')) and not re.match(r'\s*[ijkt]\s*=', upcoming))
        if not stack and c == '.' and i+1 < len(raw) and re.match(r'\s+[A-Z][a-z]{2,}\b', raw[i+1:]):
            split = True
        if split:
            if ''.join(buf).strip(): parts.append(''.join(buf).strip())
            buf = []
        else: buf.append(c)
    if ''.join(buf).strip(): parts.append(''.join(buf).strip())
    return parts


def _matrix(m):
    data = json.loads(m[0])
    if not data or len(data)>20 or not all(isinstance(row,list) and len(row)==len(data[0]) and all(isinstance(v,(int,float)) and not isinstance(v,bool) for v in row) for row in data):
        raise UncertainNotation('Nonrectangular matrix')
    return r'\begin{bmatrix}'+'\n'+(' '+r'\\'+'\n').join(' & '.join(str(v) for v in row) for row in data)+'\n'+r'\end{bmatrix}'


class _Legacy:
    """A notation printer, not a CAS: it never simplifies or evaluates."""
    def __init__(self, source, starred=(), aliases=None):
        self.s, self.i, self.starred = source, 0, set(starred)
        self.aliases = aliases or {}

    def group(self, opening):
        close = {'(':')','[':']','{':'}','|':'|'}[opening]
        start, depth = self.i, 1
        self.i += 1
        begin = self.i
        while self.i < len(self.s):
            c = self.s[self.i]
            if c == close:
                depth -= 1
                if depth == 0:
                    text = self.s[begin:self.i]; self.i += 1
                    return _Legacy(text, self.starred, self.aliases).run()
            elif c == opening and opening != '|': depth += 1
            self.i += 1
        raise UncertainNotation('Unbalanced source group at '+str(start))

    def atom(self, subscript=False):
        while self.i < len(self.s) and self.s[self.i].isspace(): self.i += 1
        if self.i >= len(self.s): raise UncertainNotation('Missing script')
        c = self.s[self.i]
        if subscript:
            # Legacy indices such as 0t and i1 are one complete subscript,
            # whereas an exponent 2x still means exponent 2 followed by x.
            index=re.match(r'(?:[A-Za-z]+|[0-9]+[A-Za-z])[A-Za-z0-9]*(?:,[ijktqr](?:[+-]\d+)?)?',self.s[self.i:])
            if index and not (index[0] in ASCII_GREEK and self.s[self.i+len(index[0]):self.i+len(index[0])+1]=='_'):
                self.i+=len(index[0])
                return ','.join(self.word(part,script=True) if re.fullmatch(r'[A-Za-z0-9]+',part) else part for part in index[0].split(','))
        if c in '{(':
            # Explicit dimension labels are not coordinate names (4x1 != 4*x_1).
            dim = re.match(r'[({](\d+)[x×](\d+)[)}]', self.s[self.i:])
            if dim:
                self.i += len(dim[0]); return dim[1]+r'\times '+dim[2]
            return self.group(c)
        if c == '|':
            return r'\lvert '+self.group(c)+r'\rvert'
        if c in '+-−':
            self.i += 1
            return ('-' if c == '−' else c)+self.atom()
        m = re.match(r'\d+(?:\.\d+)?', self.s[self.i:])
        if m:
            self.i += len(m[0]); return m[0]
        if c in GREEK:
            self.i += 1; return '\\'+GREEK[c]
        m = re.match(r'[A-Za-z]+\d*', self.s[self.i:])
        if not m: raise UncertainNotation('Unsupported script')
        self.i += len(m[0])
        val = self.word(m[0], script=True)
        # A function in an exponent binds its entire argument: ^abs(i-j).
        if m[0] in FUNCTIONS and self.i<len(self.s) and self.s[self.i]=='(':
            inner=self.group('(')
            return self.function(m[0],inner)
        return val

    def function(self, name, inner):
        if name=='sqrt': return r'\sqrt{'+inner+'}'
        if name=='abs': return r'\lvert '+inner+r'\rvert'
        if name=='floor': return r'\lfloor '+inner+r'\rfloor'
        if name=='ceil': return r'\lceil '+inner+r'\rceil'
        return self.word(name)+'('+inner+')'

    def word(self, word, script=False):
        if word in ASCII_GREEK: return '\\'+ASCII_GREEK[word]
        if word in ('infinity','infty'): return r'\infty'
        if word in ('sum','prod','Integral','integral'): return {'sum':r'\sum','prod':r'\prod','Integral':r'\int','integral':r'\int'}[word]
        if word in ('exp','log','ln','sin','cos','tan','tanh','sinh','cosh','min','max','inf','sup'): return '\\'+word
        if word in ('Normal','N') and (self.s[self.i:self.i+1] in ('(','_')): return r'\mathcal{N}'
        if word in DISTRIBUTIONS or word in FUNCTIONS or word=='SD': return r'\mathrm{'+word+'}'
        if word=='E' and self.s[self.i:self.i+1] in ('[','('): return r'\mathbb{E}'
        if not script and word in ('in','approx','mod'): return {'in':r'\in ','approx':r'\approx ','mod':r'\bmod '}[word]
        if not script and word in WORDS: return r'\text{ '+word+' }'
        m = re.fullmatch(r'([A-Za-z]|'+ '|'.join(ASCII_GREEK)+r')(\d+)',word)
        if m and not script:
            if self.s[self.i:self.i+1]=='_':return r'\mathrm{'+word+'}'
            head = self.word(m[1],script=True)
            if m[1]=='N' and self.s[self.i:self.i+1]=='(': head=r'\mathcal{N}'
            return head+'_{'+m[2]+'}'
        if re.fullmatch(r'[A-Z]{2,}',word) and word not in {'ATE','CATE','ATT','ATC','NDE','NIE','LATE','CDF','PDF','SD','IID'}: return word
        if len(word)==1 or (script and re.fullmatch(r'[ijktnmpqrs0-9]+',word)): return word
        # Do not split identifiers like raw, observed, source into products.
        return r'\mathrm{'+word+'}'

    def run(self):
        out=[]
        while self.i < len(self.s):
            c=self.s[self.i]
            if c.isspace(): out.append(' '); self.i+=1; continue
            matrix=MATRIX_RX.match(self.s,self.i)
            if matrix:
                out.append(_matrix(matrix)); self.i=matrix.end(); continue
            if self.s.startswith('**',self.i):
                self.i+=2; exponent=self.atom()
                if self.s[self.i:self.i+2]=='**':raise UncertainNotation('Chained powers require explicit parentheses')
                out.append('^{'+exponent+'}');continue
            if c in '_^':
                self.i+=1
                value=self.atom(subscript=(c=='_'))
                if self.i<len(self.s) and self.s[self.i]==c:
                    raise UncertainNotation('Repeated script without explicit grouping')
                out.append(c+'{'+value+'}');continue
            if c in SCRIPTS or c in SUPERS:
                table=SCRIPTS if c in SCRIPTS else SUPERS; chars=[]
                while self.i<len(self.s) and self.s[self.i] in table:
                    chars.append(table[self.s[self.i]]);self.i+=1
                out.append(('_' if table is SCRIPTS else '^')+'{'+''.join(chars)+'}');continue
            if c=='ᵀ': out.append(r'^{\top}');self.i+=1;continue
            if c == 'Σ' and re.match(r'(?:_[{][^}]*=|[₀-₉ⱼₖᵢ₌]*₌)', self.s[self.i+1:]):
                out.append(r'\sum'); self.i += 1; continue
            if c in GREEK:
                # Only separately named error symbols may acquire a display
                # subscript. In particular κs and βA are not κ_s and β_A.
                alias = next((name for name in sorted(self.aliases,key=len,reverse=True)
                              if self.s.startswith(name,self.i) and
                              not re.match(r'[A-Za-z0-9]',self.s[self.i+len(name):self.i+len(name)+1])),None)
                if alias:
                    out.append(self.aliases[alias]); self.i += len(alias); continue
                suffix = re.match(r'\d+',self.s[self.i+1:])
                if suffix:
                    out.append('\\'+GREEK[c]+'_{'+suffix[0]+'}');self.i+=1+len(suffix[0]);continue
                if c in 'εϵ' and re.match(r'[A-Za-z]',self.s[self.i+1:self.i+2]):
                    raise UncertainNotation('Undeclared compound error symbol')
                out.append('\\'+GREEK[c]+' ');self.i+=1;continue
            if c=='√':
                self.i+=1;out.append(r'\sqrt{'+self.atom()+'}');continue
            # Probability names such as p0Y are identifiers, not p_0 times Y.
            named=re.match(r'[a-z][a-zA-Z]*\d+[A-Za-z][A-Za-z0-9]*',self.s[self.i:])
            if named:
                out.append(r'\mathrm{'+named[0]+'}');self.i+=len(named[0]);continue
            m=re.match(r'[A-Za-z]+\d*', self.s[self.i:])
            if m:
                word=m[0]; self.i+=len(word)
                if word in ('sqrt','abs','floor','ceil') and self.s[self.i:self.i+1]=='(':
                    out.append(self.function(word,self.group('(')))
                else: out.append(self.word(word))
                continue
            m=re.match(r'(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?',self.s[self.i:])
            if m:
                out.append(m[0]);self.i+=len(m[0]);continue
            if self.s.startswith('...',self.i):out.append(r'\ldots ');self.i+=3;continue
            if self.s[self.i:self.i+2] in ('<=','>=','!='):
                out.append({'<=':r'\leq ','>=':r'\geq ','!=':r'\neq '}[self.s[self.i:self.i+2]]);self.i+=2;continue
            if c in SYMBOLS:out.append(SYMBOLS[c]);self.i+=1;continue
            if c=='*':
                before=self.s[:self.i].rstrip(); after=self.s[self.i+1:].lstrip()
                name=re.search(r'([A-Za-z]+\d*)$',before)
                if not after or after[0] in '=,;)]}~∼':out.append(r'^{\ast}')
                elif after.startswith('(') and name and name[1] in self.starred:out.append(r'^{\ast}')
                else:out.append(r'\cdot ')
                self.i+=1;continue
            if c=='{':out.append(r'\{'+self.group('{')+r'\}');continue
            if c=='\\':
                if self.s[self.i+1:self.i+2]=='{' and self.i>0 and self.s[self.i-1]=='}':
                    out.append(r'\setminus ');self.i+=1;continue
                raise UncertainNotation('Mixed or unsupported TeX')
            if c in '#%&$':out.append('\\'+c);self.i+=1;continue
            if c=='|' and self.s.count('|')==1:out.append(r'\mid ');self.i+=1;continue
            if c in '()[]|=+-,./:;!\'':out.append(c);self.i+=1;continue
            if c in '<>':out.append(c);self.i+=1;continue
            raise UncertainNotation('Unknown symbol '+repr(c))
        return ''.join(out).strip()


def plain_math_to_latex(source, starred=(), aliases=None):
    s=_unwrap(source).strip().rstrip('。，,')
    if not s or CJK.search(s) or not MATHISH.search(s):return None
    if any(x in s for x in ('<script','```')):return None
    if re.search(r'\\[A-Za-z]+',s):
        # An author-supplied TeX expression must not undergo plain-text rewriting.
        latex=_safe_latex(s)
        return latex if latex is not None and _balanced(latex) and not re.search(r'(?<!\\)\$',latex) and not DIAGNOSTIC_RX.search(latex) else None
    piecewise=re.fullmatch(r'([A-Za-z]+)\(([A-Za-z])\)\s*=\s*(.+)',s)
    if piecewise and ' on ' in piecewise[3]:
        pattern=r'(.+?)\s+on\s+([\[(][^,\]\)]*,[^,\]\)]*[\])])'
        matches=list(re.finditer(pattern,piecewise[3]))
        if matches and re.sub(pattern,'',piecewise[3]).strip(' ,.')=='':
            try:
                rows=[_Legacy(m[1].lstrip(' ,'),starred,aliases).run()+' & '+piecewise[2]+r'\in '+m[2] for m in matches]
                return piecewise[1]+'('+piecewise[2]+')='+r'\begin{cases}'+'\n'+(' '+r'\\'+'\n').join(rows)+'\n'+r'\end{cases}'
            except ValueError:pass
    starred=set(starred)|set(re.findall(r'\b([A-Za-z]+)\*\([^()]*\)\s*=',s))
    # Preserve complete prose outside math rather than running English together.
    words=re.findall(r'\b[A-Za-z]{3,}\b',s)
    known=set(ASCII_GREEK)|FUNCTIONS|DISTRIBUTIONS|WORDS|{'Sigma','Integral','sum','prod','infinity','approx','mod'}
    if sum(w not in known for w in words)>4:return None
    try:
        result=_Legacy(s,starred,aliases).run()
    except (ValueError,RecursionError):return None
    if not _balanced(result) or DIAGNOSTIC_RX.search(result):return None
    result=re.sub(r'(\\(?:sim|in|notin|leq|geq|neq|approx|propto|sum))\s{2,}',lambda m:m[1]+' ',result)
    # Keep TeX control words separate without altering variable boundaries.
    return re.sub(r'\\(alpha|beta|gamma|delta|varepsilon|zeta|eta|theta|kappa|lambda|mu|nu|xi|pi|rho|sigma|tau|phi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Phi|Psi|Omega)\s+(?=[^A-Za-z]|$)',r'\\\1',result)


def formatted_blocks(entry, starred=(), aliases=None):
    if isinstance(entry,dict) and entry.get('latex'):
        latex=_safe_latex(entry['latex'])
        if latex is not None and _balanced(latex) and '$' not in latex and '```' not in latex and not re.search(r'(?<!\\)\$',latex):
            return [('math',latex)]+([('text',str(entry['notes']))] if entry.get('notes') else [])
        return [('source',str(entry['latex']))]
    raw=original_equation(entry).strip()
    if raw in _REVIEWED_IV_PRODUCTS:
        blocks = [('math', _REVIEWED_IV_PRODUCTS[raw])]
        if isinstance(entry, dict) and entry.get('notes'):
            blocks.append(('text', str(entry['notes'])))
        return blocks
    if raw in _REVIEWED_SUMS:raw=raw.replace('Σ','∑')
    # Mixed-language descriptions frequently enclose the actual formulas in
    # backticks. Keep every surrounding note; do not discard the whole equation.
    spans=list(re.finditer(r'`([^`\n]+)`',raw))
    if spans and not (len(spans)==1 and spans[0].span()==(0,len(raw))):
        remainder=re.sub(r'`[^`\n]+`','',raw)
        number=re.match(r'^\s*(\d+)\.',remainder)
        punctuation=re.sub(r'^\s*\d+\.','',remainder).strip(' ，。;；,.')
        if not punctuation:
            blocks=[('label','Step '+number[1])] if number else []
            for span in spans:
                latex=plain_math_to_latex(span[1],starred,aliases)
                blocks.append(('math',latex) if latex else ('source',span[1]))
            return blocks
        # Keep prose together. Source-authored scalar names and lists remain
        # inline code; complete mathematical expressions become inline math.
        parts=[];pos=0
        for span in spans:
            parts.append(html.escape(raw[pos:span.start()]))
            inner=span[1]
            latex=(aliases or {}).get(inner) or plain_math_to_latex(inner,starred,aliases)
            parts.append('$`'+latex+'`$' if latex else '<code>'+html.escape(inner)+'</code>')
            pos=span.end()
        parts.append(html.escape(raw[pos:]))
        return [('mixed',''.join(parts))]
    blocks=[]
    for seg in _split_legacy(_unwrap(raw)):
        heading=re.match(r'^(Additive|Nonadditive|Non-additive)\s*:\s*(.+)',seg,re.I)
        if heading:blocks.append(('label',heading[1]));seg=heading[2]
        trailer=re.search(r',?\s*(?:mutually independent|independent(?:ly)? (?:of|from|across) .+|independent individuals)\.?$',seg,re.I)
        plain=None
        if trailer:
            seg,plain=seg[:trailer.start()].rstrip(', '),trailer[0].strip(' ,.')
        iid=re.match(r'^(.*?)\s+(?:iid|i\.i\.d\.)\s*(?:[~∼]\s*)?((?:Normal|Uniform|Bernoulli|Poisson|Binomial|N\d*)\s*\(.+)$',seg,re.I)
        if iid:
            head=plain_math_to_latex(iid[1]+'=0',starred,aliases);tail=plain_math_to_latex('Q~'+iid[2],starred,aliases)
            if head and tail:
                blocks.append(('math',head.rsplit('=',1)[0]+r'\overset{\mathrm{iid}}{\sim} '+tail.split(r'\sim',1)[1].strip()))
                if plain:blocks.append(('text',plain))
                continue
        latex=plain_math_to_latex(seg,starred,aliases)
        if seg:blocks.append(('math',latex) if latex else ('source' if MATHISH.search(seg) else 'text',seg))
        if plain:blocks.append(('text',plain))
    if isinstance(entry,dict) and entry.get('notes'):blocks.append(('text',str(entry['notes'])))
    return blocks


def _align_assignments(blocks):
    if not 2<=len(blocks)<=4 or any(k!='math' for k,_ in blocks):return None
    rows=[]
    for _,latex in blocks:
        m=re.fullmatch(r'([A-Za-z](?:_\{[A-Za-z0-9]+\})?)=(.+)',latex)
        if not m:return None
        rows.append(m[1]+' &= '+m[2])
    return r'\begin{aligned}'+'\n'+(' '+r'\\'+'\n').join(rows)+'\n'+r'\end{aligned}'


def equation_markdown(entries, include_source=True, source_entries=None):
    """Render without modifying source objects or dropping scenario labels.

    source_entries is the unchanged scientific record, before English display
    substitutions. Existing curated LaTeX stays intact. A missing translation
    falls back to the original expression, not an empty placeholder.
    """
    originals=list(entries if source_entries is None else source_entries)
    display=list(entries)
    if len(display)!=len(originals):
        raise ValueError('Equation display/source count mismatch')
    starred=set()
    for entry in originals:
        starred.update(re.findall(r'\b([A-Za-z]+)\*\([^()]*\)\s*=',original_equation(entry)))
    # Source authors explicitly identify these error terms in standalone code
    # spans or distribution declarations; do not guess from an occurrence in
    # an outcome equation. This affects display only, never the source record.
    aliases={}
    for original in originals:
        raw=original_equation(original)
        for span in re.findall(r'`([^`]+)`',raw):
            names=re.split(r'[,，]',span)
            if all(re.fullmatch(r'[εϵ][A-Za-z]+',n.strip()) for n in names):
                for n in names:
                    n=n.strip();aliases[n]=r'\varepsilon_{'+n[1:]+'}'
        for match in re.finditer(r'([εϵ][A-Za-z]+)(?=\s*[~∼])',raw):
            n=match[1];aliases[n]=r'\varepsilon_{'+n[1:]+'}'
    source_text='\n'.join(original_equation(x) for x in originals)
    if '所有下述高斯误差' in source_text:
        for n in re.findall(r'[εϵ][A-Z][A-Za-z0-9]*',source_text):
            aliases[n]=r'\varepsilon_{'+n[1:]+'}'
    out=[]
    for entry,source in zip(display,originals):
        pending='transcription pending' in original_equation(entry)
        original=original_equation(source)
        pending_cjk=bool(pending and CJK.search(original))
        if pending and not pending_cjk:entry=source
        label=(entry.get('label') if isinstance(entry,dict) else None) or (source.get('label') if isinstance(source,dict) else None)
        if label and not CJK.search(str(label)):out.extend(['**'+html.escape(str(label))+'**',''])
        if pending_cjk:
            # Only extract author-delimited fragments without CJK; preserve all
            # untranslated context in the linked original scientific JSON.
            out.extend(['English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.', ''])
            blocks=[]
            for span in re.findall(r'\x60([^\x60\n]+)\x60', original):
                if not CJK.search(span):
                    blocks.extend(formatted_blocks(span,starred,aliases))
        else:
            blocks=formatted_blocks(entry,starred,aliases)
        aligned=_align_assignments(blocks)
        if aligned:blocks=[('math',aligned)]
        for kind,expr in blocks:
            if kind=='math':out.extend(['```math',expr,'```',''])
            elif kind=='mixed':out.extend([expr,''])
            elif kind=='label':out.extend(['**'+html.escape(expr)+'**',''])
            elif kind=='source':
                out.extend(['Source notation retained without guessing:', '', '<pre>'+html.escape(expr)+'</pre>',''])
            else:out.extend([html.escape(expr),''])
    if not out:return ['- Unknown — source review required','']
    if include_source:
        out.extend(['<details>','<summary>Original source equations (verbatim)</summary>','',
                    '<pre>',html.escape('\n'.join(original_equation(x) for x in originals)),
                    '</pre>','','</details>',''])
    return out
