'use strict';
// Pause all Home SVG animations when out of view or when motion is reduced.
(() => {
  const home = document.getElementById('home');
  const svg = home?.querySelector('.home-ambient');
  if (!svg || typeof svg.pauseAnimations !== 'function') return;
  const media = window.matchMedia('(prefers-reduced-motion: reduce)');
  let lastPaused = null;
  const sync = () => {
    const paused = media.matches || document.hidden || home.hidden;
    if (paused === lastPaused) return;
    lastPaused = paused;
    if (paused) svg.pauseAnimations();
    else svg.unpauseAnimations();
  };
  if (media.addEventListener) media.addEventListener('change', sync);
  else if (media.addListener) media.addListener(sync);
  document.addEventListener('visibilitychange', sync);
  new MutationObserver(sync).observe(home, { attributes: true, attributeFilter: ['hidden'] });
  sync();
})();
