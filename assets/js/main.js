(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.documentElement.classList.add('has-js');

  const progress = document.createElement('div');
  progress.className = 'scroll-progress';
  progress.setAttribute('aria-hidden', 'true');
  document.body.prepend(progress);

  const updateProgress = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const value = scrollable > 0 ? window.scrollY / scrollable : 0;
    progress.style.transform = `scaleX(${value})`;
    document.body.classList.toggle('is-scrolled', window.scrollY > 24);
  };

  updateProgress();
  window.addEventListener('scroll', updateProgress, { passive: true });

  if (!reduceMotion) {
    const revealTargets = document.querySelectorAll(
      '.section-heading, .project-card, .experience-card, .process-card, .skill-card, .stats__item, .case-section, .case-cover, .cta-panel, .page-hero > .container-site'
    );

    revealTargets.forEach((element, index) => {
      element.classList.add('reveal');
      element.style.setProperty('--reveal-delay', `${Math.min(index % 4, 3) * 70}ms`);
    });

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

    revealTargets.forEach((element) => observer.observe(element));

    document.querySelectorAll('.project-card__media, .case-cover').forEach((surface) => {
      surface.addEventListener('pointermove', (event) => {
        const bounds = surface.getBoundingClientRect();
        surface.style.setProperty('--pointer-x', `${((event.clientX - bounds.left) / bounds.width) * 100}%`);
        surface.style.setProperty('--pointer-y', `${((event.clientY - bounds.top) / bounds.height) * 100}%`);
      });
    });

    document.querySelectorAll('a[href]').forEach((link) => {
      const url = new URL(link.href, window.location.href);
      const isSameSitePage = url.origin === window.location.origin &&
        url.pathname.endsWith('.html') && !link.target && url.href !== window.location.href;

      if (!isSameSitePage) return;

      link.addEventListener('click', (event) => {
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        document.body.classList.add('is-leaving');
        window.setTimeout(() => { window.location.href = link.href; }, 360);
      });
    });
  }

  window.addEventListener('pageshow', () => document.body.classList.remove('is-leaving'));
})();
