# Shammas CB — Personal Portfolio

A polished, responsive, static portfolio website for Shammas CB, a software developer and AI enthusiast.
The site uses HTML, CSS, JavaScript, and the Bootstrap 5.3.3 responsive grid so it can be deployed directly to GitHub Pages without a build service.

## Included

- Dark, futuristic visual system with blue and purple gradients.
- Responsive navigation with a mobile menu.
- Professional navigation links for GitHub and LinkedIn.
- Bootstrap responsive grid support for the hero layout, with custom CSS preserving the visual design.
- Hero, about, skills/toolkit, language proficiency, projects, education/certifications, contact, and footer sections.
- Scroll reveal animation, scroll progress indicator, project hover states, and accessible form feedback.
- Grouped skills directory, language proficiency panel, and featured project layout for easier scanning.
- Premium animated SVG visuals for Resume Analyser, AI HOME BRAIN, and the LLM Project cards; they are local, lightweight, and work without an image CDN.
- The AI HOME BRAIN card credits both team members: Shammas as Project Creator and Fathah as Project Contributor, with Fathah's supplied LinkedIn and email links.
- Premium animated SVG icons for the five toolkit cards: AI/ML engineering, backend development, frontend development, Data & NLP, and Tools & collaboration.
- The Skills directory groups also have premium animated SVG visuals for Programming & web, AI & data, Tools & collaboration, and Professional strengths.
- The Journey timeline also uses premium animated SVG visuals for the internship, BCA education, AI certification, and current learning entries.
- A branded SCB technology favicon is available in SVG, PNG, ICO, and Apple touch-icon formats and is referenced from the page head.
- Verified profile, internship, education, certification, and direct contact details supplied by Shammas CB, plus honest placeholders for project links that were not provided.
- Footer social icons link to Instagram, LinkedIn, and GitHub, with tap-to-call and tap-to-email contact links.
- Resume links in the navigation, hero, and footer open `assets/Shammas_CB_Resume.pdf` in a new tab.
- The hero uses only the supplied animated Fathah reference video at `assets/fathah-reference.mp4`; decorative cards, labels, and the previous front photo are removed. It starts muted so browsers allow autoplay, and the custom **Hear the voice** button enables the video's existing audio after one tap or click.
- No invented achievements, qualifications, testimonials, or project URLs.

## Run locally

Requirements: Node.js 22+ and Python 3.

The page loads Bootstrap 5.3.3 and the selected fonts from their public CDNs when viewed online. The custom responsive CSS remains in place as the visual layer.

If a phone shows an older layout after an update, reload the address once with `?v=3` at the end, or clear the browser cache for the local page.

```bash
npm run check
python3 -m http.server 8000
```

Then open http://localhost:8000.

Or use the Makefile:

```bash
make test
make serve
```

## GitHub Pages deployment

1. Create a GitHub repository and push the contents of this folder to its default branch.
2. In the repository, open **Settings → Pages**.
3. Set the source to **Deploy from a branch**, choose the default branch and `/ (root)`, then save.
4. GitHub Pages will serve `index.html`; no build command is needed.

The `.nojekyll` file is included so GitHub Pages serves the static files exactly as written.

## Personalize before launch

- Replace the profile placeholder in `index.html` with a real image if desired.
- Replace `assets/fathah-reference.mp4` with an updated animation using the same filename if needed.
- Replace `assets/Shammas_CB_Resume.pdf` with an updated resume using the same filename when needed.
- Add more verified education and certification details as the journey grows.
- Keep the phone and email links current if contact details change.
- Add project-specific GitHub or live demo URLs only when they exist.
- Connect the contact form to a form provider or backend if real message delivery is needed. The current form validates input and provides clear front-end feedback without pretending to send email.

## Checks

The single offline check is:

```bash
npm run check
```

It validates JavaScript syntax, required files, and key user-facing content. No third-party package installation is required.
