const families = {
  ate: {title: 'Average treatment effect', question: 'What is the average treatment contrast in the declared population?', target: 'ATE = E[Y(1) − Y(0)]', spec: 'Specify treatment, outcome, covariates, population, and assignment. Randomization or observational identification, consistency, exchangeability, and positivity must match the setting.'},
  cate: {title: 'Conditional average treatment effect', question: 'What is the treatment contrast at a prespecified baseline profile?', target: 'τ(x₀) = E[Y(1) − Y(0) | X = x₀]', spec: 'Begin with a scalar CATE at a fixed supported query x₀. Define identification and local regularity conditions. Coverage at this query does not establish simultaneous coverage or an individual counterfactual effect.'},
  mediation: {title: 'Natural direct and indirect effects', question: 'How much of the treatment effect operates through a specified mediator?', target: 'NIE = E[Y(1,M(1)) − Y(1,M(0))]; NDE = E[Y(1,M(0)) − Y(0,M(0))]', spec: 'NIE and NDE are separate target records. Declare timing, support, required confounding and cross-world assumptions, and the observed-data identification formula. The mediation worked demo is planned.'},
  iv: {title: 'Instrumental variables and noncompliance', question: 'What causal effect does a valid instrument identify?', target: 'LATE = E[Y(1) − Y(0) | complier]', spec: 'For binary instrument and treatment, state relevance, independence, exclusion, and monotonicity. Other IV targets need their own specification. Weak instruments require justified inference, potentially with unbounded or disconnected confidence sets.'},
  proximal: {title: 'Proximal causal inference', question: 'Can valid proxies identify an effect despite latent confounding?', target: 'ψ = E[h(W,1,X) − h(W,0,X)]', spec: 'Define treatment-inducing and outcome-inducing proxy roles, the bridge equation, negative-control restrictions, existence, and completeness or alternative identification conditions. Weak proxies and ill-posedness are separate stress settings.'},
  did_sc: {title: 'DiD and synthetic control · distinct designs', question: 'What is the effect for a treated group or unit over a declared post-treatment period?', target: 'DiD: ATT(g,t); synthetic control: Ytreated,t(1) − Ytreated,t(0), or a declared time average', spec: 'DiD needs a specified comparison group, timing, parallel-trends and anticipation conditions. Synthetic control needs a donor pool, pre-treatment fit/model, and an inference design. They share a family label, not one estimand, estimator, or validity guarantee.'}
};

const familyButtons = [...document.querySelectorAll('[data-family]')];
function chooseFamily(key) {
  const family = families[key];
  if (!family) return;
  familyButtons.forEach(button => {
    const active = button.dataset.family === key;
    button.setAttribute('aria-selected', String(active));
    button.tabIndex = active ? 0 : -1;
  });
  document.getElementById('family-detail').setAttribute('aria-labelledby', 'family-tab-' + key);
  ['title', 'question', 'target', 'spec'].forEach(field => {
    document.getElementById('family-' + field).textContent = family[field];
  });
}
function keyboardTab(event, index, buttons, choose, key) {
  let next;
  if (['ArrowRight', 'ArrowDown'].includes(event.key)) next = (index + 1) % buttons.length;
  if (['ArrowLeft', 'ArrowUp'].includes(event.key)) next = (index - 1 + buttons.length) % buttons.length;
  if (event.key === 'Home') next = 0;
  if (event.key === 'End') next = buttons.length - 1;
  if (next !== undefined) {
    event.preventDefault();
    buttons[next].focus();
    choose(buttons[next].dataset[key]);
  }
}
familyButtons.forEach((button, index) => {
  button.addEventListener('click', () => chooseFamily(button.dataset.family));
  button.addEventListener('keydown', event => keyboardTab(event, index, familyButtons, chooseFamily, 'family'));
});
chooseFamily('ate');

const views = ['overview', 'contribute', 'evaluation', 'arena'];
const tabs = [...document.querySelectorAll('.view-tabs [data-view]')];
function chooseView(key, scroll = false) {
  if (!views.includes(key)) key = 'overview';
  document.querySelectorAll('.view-panel').forEach(panel => { panel.hidden = panel.id !== 'view-' + key; });
  tabs.forEach(button => {
    const active = button.dataset.view === key;
    button.setAttribute('aria-selected', String(active));
    button.tabIndex = active ? 0 : -1;
  });
  document.querySelectorAll('nav [data-view]').forEach(button => {
    if (button.dataset.view === key) button.setAttribute('aria-current', 'page');
    else button.removeAttribute('aria-current');
  });
  if (scroll) document.getElementById('content').scrollIntoView({block: 'start'});
  try { history.replaceState(null, '', '#' + key); } catch {}
}
document.querySelectorAll('[data-view]').forEach(button => {
  button.addEventListener('click', () => chooseView(button.dataset.view, !button.closest('.view-tabs')));
});
tabs.forEach((button, index) => {
  button.addEventListener('keydown', event => keyboardTab(event, index, tabs, chooseView, 'view'));
});
document.querySelector('.brand').addEventListener('click', event => {
  event.preventDefault();
  chooseView('overview');
  window.scrollTo({top: 0, behavior: 'instant'});
});
window.addEventListener('hashchange', () => chooseView(location.hash.slice(1)));
chooseView(location.hash.slice(1) || 'overview');

// Proposed scientific cases only: no implemented tasks or measured results.
const arenaCases = [
  {family: 'ate', target: 'ate', object: 'parameter_ci', title: 'Population ATE',
    scope: 'Scalar causal-parameter coverage over independently repeated datasets at each fixed DGP.',
    canonical: 'Randomized binary treatment, independent units, and a prespecified population contrast.',
    stress: 'Weak overlap in a separately specified observational design, with identification and nuisance conditions retained.',
    reference: 'Difference in means with a design-appropriate CI',
    stressReference: 'AIPW / DML reference under declared overlap and nuisance conditions'},
  {family: 'cate', target: 'cate_at_x0', object: 'parameter_ci', title: 'CATE at fixed query x₀',
    scope: 'Coverage at one prespecified supported query x₀ over repeated datasets; no simultaneous claim.',
    canonical: 'Randomized treatment with a correctly specified treatment-interaction model at a fixed query.',
    stress: 'Nonlinear effects or weak local support; specify smoothness, query support, and target truth.',
    reference: 'Model-based interaction contrast with a justified CI',
    stressReference: 'Local / orthogonal effect-inference reference; validity to verify'},
  {family: 'mediation', target: 'nie', object: 'parameter_ci', title: 'Natural indirect effect NIE',
    scope: 'Scalar NIE coverage over repeated datasets under the stated mediation identification model.',
    canonical: 'A simple identified mediation DGP with independently checked NIE truth and a parametric reference.',
    stress: 'Nonlinearity, treatment–mediator interaction, or limited support within a specified identification regime.',
    reference: 'Parametric mediation g-computation with a justified NIE CI',
    stressReference: 'NIE-specific reference; nuisance and interval conditions to verify'},
  {family: 'mediation', target: 'nde', object: 'parameter_ci', title: 'Natural direct effect NDE',
    scope: 'Scalar NDE coverage over repeated datasets; a separate target from NIE.',
    canonical: 'A simple identified mediation DGP with independently checked complementary NDE truth.',
    stress: 'Nonlinearity, interaction, or limited support; preserve the declared natural-effect definition.',
    reference: 'Parametric mediation g-computation with a justified NDE CI',
    stressReference: 'NDE-specific reference; nuisance and interval conditions to verify'},
  {family: 'iv', target: 'late', object: 'parameter_ci', title: 'Complier LATE',
    scope: 'Scalar local-effect coverage over repeated datasets under the declared binary-IV design.',
    canonical: 'Valid binary instrument and treatment, monotonicity, and a nonvanishing first stage.',
    stress: 'Weak first stage; permit justified unbounded confidence sets and define any disconnected-set extension.',
    reference: 'Wald ratio with an influence-function / delta CI',
    stressReference: 'Weak-IV-robust reference with a target-compatible confidence-set contract'},
  {family: 'proximal', target: 'proximal_ate', object: 'parameter_ci', title: 'Proximal population effect',
    scope: 'Scalar causal-effect coverage under the specified proxy, bridge, and sampling model.',
    canonical: 'A validated finite-dimensional bridge model with sufficiently informative proxies.',
    stress: 'Weak proxies or an ill-conditioned bridge; specify regularization and identification limits.',
    reference: 'Bridge-equation / GMM reference with a justified CI',
    stressReference: 'Regularized proximal reference; interval validity to verify'},
  {family: 'did_sc', target: 'did_att', object: 'parameter_ci', title: 'DiD · treated-group ATT',
    scope: 'Treated-group ATT coverage over repeated panel datasets, preserving within-unit dependence.',
    canonical: 'Two-period treatment and comparison groups with parallel trends, no anticipation, and a declared sampling design.',
    stress: 'Staggered adoption or heterogeneous effects requires a separate group–time target and comparison rule.',
    reference: 'Design-matched DiD ATT estimator with a dependence-aware CI',
    stressReference: 'Group–time ATT reference under an explicit adoption design'},
  {family: 'did_sc', target: 'sc_effect', object: 'parameter_ci', title: 'Synthetic control · treated-unit effect',
    scope: 'Declared treated-unit time-specific or post-period average effect; the repeated-panel or assignment law must be specified.',
    canonical: 'A declared donor pool and pre-treatment factor/model structure with checked counterfactual truth.',
    stress: 'Limited donor support or imperfect pre-treatment fit; reassess the model and inference conditions.',
    reference: 'Synthetic-control reference with inference justified by the declared design',
    stressReference: 'Design-matched synthetic-control sensitivity / inference reference; validity to verify'}
];
const arenaFamily = document.getElementById('arena-family');
const arenaTarget = document.getElementById('arena-target');
const arenaRegime = document.getElementById('arena-regime');
function appendText(parent, tag, value, className) {
  const element = document.createElement(tag);
  element.textContent = value;
  if (className) element.className = className;
  parent.appendChild(element);
  return element;
}
function updateArenaTargets() {
  const previous = arenaTarget.value;
  const cases = arenaCases.filter(candidate => candidate.family === arenaFamily.value);
  arenaTarget.replaceChildren();
  cases.forEach(candidate => {
    const option = appendText(arenaTarget, 'option', candidate.title);
    option.value = candidate.target;
  });
  arenaTarget.value = cases.some(candidate => candidate.target === previous) ? previous : (cases[0]?.target || '');
  arenaTarget.disabled = cases.length === 0;
}
function renderArena() {
  const family = arenaFamily.value;
  const target = arenaTarget.value;
  const regime = arenaRegime.value;
  const selected = ['canonical', 'stress'].includes(regime)
    ? arenaCases.find(candidate => candidate.family === family && candidate.target === target) : null;
  const context = document.getElementById('arena-context');
  const body = document.getElementById('arena-body');
  const empty = document.getElementById('arena-empty');
  const table = document.querySelector('.arena-table');
  context.replaceChildren();
  body.replaceChildren();
  empty.hidden = Boolean(selected);
  table.hidden = !selected;
  if (!selected) {
    appendText(context, 'p', 'No proposed case for the selected family, estimand, and regime.', 'small');
    return;
  }
  appendText(context, 'h3', selected.title);
  appendText(context, 'p', (regime === 'canonical' ? 'Canonical setting: ' : 'Stress setting: ') + selected[regime]);
  appendText(context, 'p', 'Coverage scope: ' + selected.scope, 'arena-scope');
  appendText(context, 'p', 'Parameter CI · nominal level, replication budget, and reference validation pending task development.', 'small');
  document.getElementById('arena-caption').textContent = selected.title + ' · ' + (regime === 'canonical' ? 'Canonical' : 'Stress') + ' · 3 pending comparison slots';
  const slots = [
    ['Classical / reference', regime === 'canonical' ? selected.reference : selected.stressReference],
    ['PFN · native', 'Task-compatible native estimate and CI; implementation pending'],
    ['PFN · adapted', 'Declared calibration, correction, or resampling wrapper; implementation pending']
  ];
  slots.forEach(([name, implementation]) => {
    const row = document.createElement('tr');
    const heading = appendText(row, 'th', name);
    heading.scope = 'row';
    appendText(row, 'td', implementation);
    const status = appendText(row, 'td', '');
    appendText(status, 'span', 'Pending', 'pending-badge');
    ['Coverage', '95% Monte Carlo band', 'Interval length', 'RMSE', 'Failures', 'Runtime'].forEach(metric => {
      const cell = appendText(row, 'td', '—', 'unmeasured');
      cell.setAttribute('aria-label', metric + ': not measured');
    });
    body.appendChild(row);
  });
}
arenaFamily.addEventListener('change', () => { updateArenaTargets(); renderArena(); });
arenaTarget.addEventListener('change', renderArena);
arenaRegime.addEventListener('change', renderArena);
updateArenaTargets();
renderArena();
