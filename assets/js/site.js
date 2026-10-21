/*
  PARALLAX site script: header menu, current-section highlight in the case-study index,
  discreet reveal on long pages and the rings drawing in page heroes.
  Everything is readable without JavaScript; motion is skipped with prefers-reduced-motion.
*/
(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const english = document.documentElement.lang === 'en';

  /* Language switch: keep the section being read (both versions share the same ids). */
  document.querySelectorAll('[data-lang-switch]').forEach((link) => {
    link.addEventListener('click', () => {
      if (location.hash && !link.hash) link.hash = location.hash;
    });
  });

  /* Menu: Escape, a click outside or a link closes it; Tab stays inside while open. */
  const button = document.querySelector('.px-menu-button');
  const panel = document.getElementById('site-menu');
  if (button && panel) {
    const links = () => [...panel.querySelectorAll('a')];
    const open = () => {
      panel.hidden = false;
      button.setAttribute('aria-expanded', 'true');
      button.setAttribute('aria-label', english ? 'Close the menu' : 'Chiudi il menu');
      links()[0]?.focus();
    };
    const close = (returnFocus) => {
      panel.hidden = true;
      button.setAttribute('aria-expanded', 'false');
      button.setAttribute('aria-label', english ? 'Open the menu' : 'Apri il menu');
      if (returnFocus) button.focus();
    };
    button.addEventListener('click', () => (panel.hidden ? open() : close(true)));
    panel.addEventListener('click', (event) => {
      if (event.target.closest('a')) close(false);
    });
    document.addEventListener('click', (event) => {
      if (!panel.hidden && !event.target.closest('.px-header')) close(false);
    });
    document.addEventListener('keydown', (event) => {
      if (panel.hidden) return;
      if (event.key === 'Escape') {
        event.preventDefault();
        close(true);
        return;
      }
      if (event.key !== 'Tab') return;
      const items = [button, ...links()];
      const first = items[0];
      const last = items[items.length - 1];
      const active = document.activeElement;
      if (event.shiftKey && active === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && active === last) {
        event.preventDefault();
        first.focus();
      } else if (!items.includes(active)) {
        event.preventDefault();
        first.focus();
      }
    });
    window.matchMedia('(min-width: 900px)').addEventListener('change', (event) => {
      if (event.matches && !panel.hidden) close(false);
    });
  }

  /* Deep links (#section) opened directly: web fonts can shift the layout after the first jump. */
  if (location.hash && document.fonts) {
    document.fonts.ready.then(() => {
      const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (target) target.scrollIntoView({ block: 'start', behavior: 'instant' });
    });
  }

  /* Case-study index: highlight the section being read. */
  const indexLinks = [...document.querySelectorAll('.case-layout__index a[href^="#"]')];
  if (indexLinks.length && 'IntersectionObserver' in window) {
    const byId = new Map(indexLinks.map((link) => [decodeURIComponent(link.hash.slice(1)), link]));
    const sections = [...byId.keys()].map((id) => document.getElementById(id)).filter(Boolean);
    const setCurrent = (id) => {
      indexLinks.forEach((link) => {
        const isCurrent = link.hash.slice(1) === id;
        link.classList.toggle('is-current', isCurrent);
        if (isCurrent) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    };
    const visible = new Set();
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) visible.add(entry.target.id);
        else visible.delete(entry.target.id);
      });
      const current = sections.find((section) => visible.has(section.id));
      if (current) setCurrent(current.id);
    }, { rootMargin: '-25% 0px -60% 0px' });
    sections.forEach((section) => observer.observe(section));
  }

  if (reduceMotion) return;

  /* Page hero rings: drawn once from their midpoint, as on the home page. */
  document.querySelectorAll('.page-hero__rings path').forEach((path, index) => {
    if (typeof path.animate !== 'function' || typeof path.getTotalLength !== 'function') return;
    const length = path.getTotalLength();
    path.animate(
      [
        { strokeDasharray: `0px ${length}px`, strokeDashoffset: `${-length / 2}px` },
        { strokeDasharray: `${length}px ${length}px`, strokeDashoffset: '0px' }
      ],
      { duration: 1300, delay: 120 + index * 50, easing: 'cubic-bezier(.62,.04,.22,1)', fill: 'backwards' }
    );
  });

  /* Discreet reveal of content blocks below the first screen. Content stays visible without JS. */
  if (!('IntersectionObserver' in window)) return;
  const targets = document.querySelectorAll(
    '.case-section, .project-card, .case-summary, .section-heading, .experience-card, .form-card, .professional-projects article, .responsibility-grid article, .timeline > li, .cases > li'
  );
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      revealObserver.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
  targets.forEach((target) => {
    const rect = target.getBoundingClientRect();
    if (rect.top < window.innerHeight) return; // already on screen: never hide it
    target.classList.add('px-reveal');
    revealObserver.observe(target);
  });
})();
