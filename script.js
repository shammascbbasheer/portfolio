const header = document.querySelector('.site-header');
const menuToggle = document.querySelector('.menu-toggle');
const siteNav = document.querySelector('.site-nav');
const progressBar = document.querySelector('.scroll-progress');
const form = document.querySelector('#contact-form');
const formStatus = document.querySelector('#form-status');
const year = document.querySelector('#current-year');
const presenterVideo = document.querySelector('#presenter-video');
const voiceButton = document.querySelector('.video-voice-button');
const mobileViewport = window.matchMedia('(max-width: 700px)');

function updateScrollState() {
  const pageHeight = document.documentElement.scrollHeight - window.innerHeight;
  const progress = pageHeight > 0 ? (window.scrollY / pageHeight) * 100 : 0;

  header?.classList.toggle('is-scrolled', window.scrollY > 12);
  if (progressBar) progressBar.style.width = `${progress}%`;
}

function closeMenu() {
  if (!menuToggle || !siteNav) return;
  menuToggle.setAttribute('aria-expanded', 'false');
  siteNav.classList.remove('is-open');
  document.body.style.overflow = '';
}

window.addEventListener('scroll', updateScrollState, { passive: true });
window.addEventListener('resize', () => {
  updateScrollState();
  if (!mobileViewport.matches) closeMenu();
});
mobileViewport.addEventListener?.('change', () => {
  if (!mobileViewport.matches) closeMenu();
});
updateScrollState();

menuToggle?.addEventListener('click', () => {
  const isOpen = menuToggle.getAttribute('aria-expanded') === 'true';
  menuToggle.setAttribute('aria-expanded', String(!isOpen));
  siteNav?.classList.toggle('is-open', !isOpen);
  document.body.style.overflow = isOpen ? '' : 'hidden';
});

siteNav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));

voiceButton?.addEventListener('click', () => {
  if (!presenterVideo) return;

  const voiceEnabled = voiceButton.getAttribute('aria-pressed') === 'true';
  presenterVideo.muted = voiceEnabled;
  presenterVideo.volume = 1;
  voiceButton.setAttribute('aria-pressed', String(!voiceEnabled));
  voiceButton.innerHTML = voiceEnabled
    ? '<span aria-hidden="true">🔊</span> Hear the voice'
    : '<span aria-hidden="true">🔇</span> Mute voice';
  presenterVideo.play().catch(() => {
    voiceButton.setAttribute('aria-pressed', 'false');
    presenterVideo.muted = true;
    voiceButton.innerHTML = '<span aria-hidden="true">🔊</span> Hear the voice';
  });
});

const revealObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  },
  { threshold: 0.12 },
);

document.querySelectorAll('.reveal').forEach((element) => revealObserver.observe(element));

year.textContent = new Date().getFullYear();

form?.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const name = String(formData.get('name') || '').trim();
  const email = String(formData.get('email') || '').trim();
  const message = String(formData.get('message') || '').trim();

  if (!name || !email || !message) {
    formStatus.textContent = 'Please complete all fields before sending.';
    formStatus.classList.add('error');
    return;
  }

  formStatus.classList.remove('error');
  formStatus.textContent = `Thanks, ${name.split(' ')[0]} — your message is ready. Add an email address in the page to enable delivery.`;
  form.reset();
});
