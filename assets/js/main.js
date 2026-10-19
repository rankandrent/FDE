// tkxel FDE — site interactions. Every block checks its elements exist, so this one file works on every page.

// Header: solid background once scrolled past the hero, services mega menu, mobile menu
(function () {
  const hdr = document.querySelector('[data-hdr]');
  if (!hdr) return;
  const hero = document.querySelector('[data-hero]');
  const update = () => {
    const limit = hero ? hero.offsetHeight - 80 : 10;
    hdr.classList.toggle('is-solid', window.scrollY > limit);
  };
  update();
  window.addEventListener('scroll', update, { passive: true });

  const btn = document.querySelector('[data-mega-btn]');
  const mega = document.querySelector('[data-mega]');
  const setMega = (open) => {
    mega.hidden = !open;
    btn.setAttribute('aria-expanded', String(open));
  };
  btn.addEventListener('click', () => setMega(mega.hidden));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMega(false); });
  document.addEventListener('click', (e) => { if (!e.target.closest('.hdr__mega-wrap')) setMega(false); });

  const burger = document.querySelector('[data-burger]');
  burger.addEventListener('click', () => {
    const open = hdr.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', String(open));
  });
})();

// Fade-and-rise on section entry
(function () {
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    }
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));
})();

// Sticky section nav: highlight the section currently in view
(function () {
  const links = [...document.querySelectorAll('[data-snav] a')];
  if (!links.length) return;
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) links.forEach((l) => l.classList.toggle('is-active', l.dataset.anchor === e.target.id));
    }
  }, { rootMargin: '-45% 0px -50% 0px' });
  links.forEach((l) => {
    const target = document.getElementById(l.dataset.anchor);
    if (target) io.observe(target);
  });
})();

// Service grid: prev / next arrows scroll the card row
document.querySelectorAll('.sg').forEach((sec) => {
  const row = sec.querySelector('[data-sg-row]');
  const step = () => (row.querySelector('.sg__card')?.offsetWidth ?? 360) + 24;
  sec.querySelector('[data-sg-prev]')?.addEventListener('click', () => row.scrollBy({ left: -step(), behavior: 'smooth' }));
  sec.querySelector('[data-sg-next]')?.addEventListener('click', () => row.scrollBy({ left: step(), behavior: 'smooth' }));
});

// Process timeline: hover or tap a step to expand it and light the matching layer
document.querySelectorAll('[data-pt]').forEach((sec) => {
  const steps = [...sec.querySelectorAll('[data-pt-step]')];
  const layers = [...sec.querySelectorAll('[data-pt-layer]')];
  const num = sec.querySelector('[data-pt-num]');
  const activate = (i) => {
    steps.forEach((s, j) => {
      s.classList.toggle('is-active', i === j);
      s.querySelector('button').setAttribute('aria-expanded', String(i === j));
    });
    layers.forEach((l, j) => l.classList.toggle('is-active', i === j));
    num.textContent = String(i + 1).padStart(2, '0');
  };
  steps.forEach((s, i) => {
    s.addEventListener('mouseenter', () => activate(i));
    s.querySelector('button').addEventListener('click', () => activate(i));
  });
});

// Lead form: posts to /api/lead (backend not built yet — see README)
document.querySelectorAll('[data-lead-form]').forEach((form) => {
  const status = form.querySelector('[data-lead-status]');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    status.textContent = 'Sending…';
    try {
      const res = await fetch(form.action, { method: 'POST', body: new FormData(form) });
      if (!res.ok) throw new Error();
      form.reset();
      status.textContent = 'Thanks — we will be in touch within one business day.';
    } catch {
      status.textContent = 'Something went wrong. Please email us instead.';
    }
  });
});

// Blog index: filter article cards by topic
document.querySelectorAll('.blog__filters').forEach((rail) => {
  const cards = [...document.querySelectorAll('[data-blog-grid] .idx__card')];
  rail.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-filter]');
    if (!btn) return;
    rail.querySelectorAll('[data-filter]').forEach((b) => {
      b.classList.toggle('is-active', b === btn);
      b.setAttribute('aria-pressed', String(b === btn));
    });
    const tag = btn.dataset.filter;
    cards.forEach((c) => { c.hidden = tag !== 'all' && !c.dataset.tags.split(' ').includes(tag); });
  });
});
