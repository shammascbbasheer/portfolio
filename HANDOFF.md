# Shammas CB Portfolio — Remaining Project Handoff

Updated: 2026-10-18

## Goal

Finish and verify the responsive personal portfolio for Shammas CB. On a real phone, the page should open at the phone width without requiring pinch-zooming out. The portfolio should keep the dark futuristic design, mobile menu, project sections, contact form feedback, and GitHub Pages compatibility.

## State

- The static portfolio is implemented from committed revision `7cf8ff7` (`docs: add portfolio handoff`).
- User-supplied profile, LinkedIn, internship, education, certification, Resume Analyser project, skills, and language details are now reflected in the page; these updates are currently uncommitted.
- The skills list is presented as a responsive, grouped Skills directory rather than an unstructured tag cloud.
- The BCA education entry is structured with separate degree, institution, university, date range, and Problem Solving skill details.
- The presentation pass now uses clearer professional navigation, role-focused toolkit cards, a wide featured Resume Analyser project layout, and direct phone/email contact links.
- The Resume Analyser card now links to the supplied live demo: `https://resumeai-analyser.vercel.app`.
- Project cards now use local premium animated SVG visuals for Resume Analyser, AI HOME BRAIN, and the LLM Project.
- Toolkit cards now use local premium animated SVG icons for AI/ML, backend, frontend, Data & NLP, and tools/collaboration.
- Skills directory groups now use local premium animated SVG visuals for Programming & web, AI & data, Tools & collaboration, and Professional strengths.
- Journey timeline entries now use local premium animated SVG visuals for the internship, BCA education, AI certification, and current learning stages.
- The page now uses a branded SCB technology favicon in SVG, PNG, ICO, and Apple touch-icon formats, with the professional tab title `Shammas CB — Software Developer & AI/ML Portfolio`.
- AI HOME BRAIN now has one shared Project team block crediting Shammas as Project Creator and Fathah as Project Contributor, with Fathah's supplied LinkedIn and email links.
- AI HOME BRAIN is now separated into an Upcoming Projects section and explicitly marked planned/not completed; it is no longer presented as selected finished work.
- A second planned item, LLM Project, is now listed beside AI HOME BRAIN under Upcoming Projects and is also marked not completed.
- Instagram is now listed in the Contact links using the canonical profile URL `https://www.instagram.com/shammas_bin_basheer/`; the supplied `/following/?hl=en` path was normalized because it opens the following list rather than the profile.
- The supplied resume PDF is bundled at `assets/Shammas_CB_Resume.pdf` and linked from the navigation, hero, and footer so visitors can open it in a new tab.
- The hero now contains only the supplied animated Fathah reference video at `assets/fathah-reference.mp4`; the previous front presenter photo, decorative labels, notes, and terminal card are no longer used by the page. A custom **Hear the voice** button unmutes the existing audio after a user tap/click; this is required because browsers block sound autoplay.
- Bootstrap 5.3.3 responsive grid is included in `index.html`.
- Custom CSS keeps the visual design and adds mobile/tablet layout rules.
- A touch-device fallback applies the mobile layout when a phone browser requests desktop mode.
- Width guards and `?v=3` cache-busting were added after the user reported that the phone still showed a laptop-sized page.
- The remaining important work is manual verification on the actual phone. Browser automation is not installed in this workspace, and no deployment has been verified.

## Important files

- `index.html` — page markup, viewport metadata, Bootstrap stylesheet, and cache-busted local assets.
- `styles.css` — visual system and responsive/mobile rules.
- `script.js` — mobile navigation, scroll effects, and contact-form feedback.
- `check_site.py` — offline content and responsive-regression checks.
- `assets/Shammas_CB_Resume.pdf` — the resume opened by the page links.
- `README.md` — setup, local run, and GitHub Pages instructions.
- `Dockerfile`, `Makefile`, `.nvmrc`, `package-lock.json` — reproducible project setup.

## Decisions

- Keep the project as a static HTML/CSS/JavaScript site; no framework build step is needed.
- Use Bootstrap only as a responsive grid layer, not as a replacement for the custom design.
- Do not invent the user's email or project URLs; use only details supplied by the user for profile, experience, education, and certifications.
- Use the LinkedIn URL supplied by the user: `https://www.linkedin.com/in/shammas-cb/`.
- Use the supplied Instagram account `shammas_bin_basheer` through its canonical profile URL.
- Use the supplied Codec Technologies internship, BCA education, and Artificial Intelligence certification details in the Journey section.
- Use the supplied Resume Analyser project details, contributor credit, and live demo URL: `https://resumeai-analyser.vercel.app`.
- Keep AI HOME BRAIN under Upcoming Projects until the user confirms it is completed and provides a project link.
- Keep LLM Project under Upcoming Projects until the user supplies confirmed implementation details or a project link.
- Use the supplied technical/professional skills and English, Malayalam, and Tamil proficiency details in the Toolkit section. Keep Bangalore University represented in Education, not as a skill.
- Keep the Skills directory grouped into Programming & Web, AI & Data, Tools & Collaboration, and Professional Strengths for scanability.
- Keep the education hierarchy clear: BCA → Bachelor of Computer Applications → Harsha Institute of Management Studies → Bangalore University → Aug 2023 — Aug 2026.
- The contact form intentionally does not pretend to send email until a real delivery service is added; direct phone and email links are available in the contact section and footer.

## Checks

Working folder: `/Users/macsolve/Desktop/personal website`
Base revision: `7cf8ff7`; current profile, LinkedIn, experience, education, certification, project, skills, and language updates are uncommitted.

- **Test — passed:** `npm run check`
  - JavaScript syntax check passed.
  - Required file/content checks passed (7 files, 35 checks), including the supplied profile, LinkedIn, internship, structured education, certification, Resume Analyser, grouped skills, language details, and resume links.
  - Professional navigation, project layout, direct contact details, footer social links, Resume Analyser live-demo, Instagram profile, and Upcoming Projects/LLM status checks passed.
  - Responsive viewport, Bootstrap grid, mobile width guard, touch-device fallback, and navigation checks passed.
- **Lint — not configured:** no lint script or lint tool is present.
- **Typecheck — not applicable:** this is a static HTML/CSS/JavaScript site with no typed source or typecheck script.
- **Build — not applicable:** GitHub Pages serves the static files directly; no build step is defined.
- **HTTP smoke check — passed:** `python3 -m http.server 8765 --bind 127.0.0.1` served `index.html?v=3` with HTTP 200.
- **Live demo smoke check — passed:** `https://resumeai-analyser.vercel.app` returned HTTP 200.
- **Instagram smoke check — passed:** `https://www.instagram.com/shammas_bin_basheer/` returned HTTP 200.
- **Manual phone check — pending:** not yet confirmed on the user's physical phone.
- **Presenter animation smoke check — pending:** `assets/fathah-reference.mp4` is bundled and referenced by the hero; the browser playback still needs a manual check.

## Resume tomorrow

On the Mac, run:

```bash
cd "/Users/macsolve/Desktop/personal website"
npm run check
python3 -m http.server 8000 --bind 0.0.0.0
```

Keep the terminal open. On the phone, connected to the same Wi-Fi, open:

```text
http://<mac-wi-fi-ip>:8000/?v=3
```

If the Mac's Wi-Fi IP has changed, get the new one with:

```bash
ipconfig getifaddr en0
```

Replace `<mac-wi-fi-ip>` with the result of the command above. If Safari/Chrome offers desktop mode, turn it off. If the page is cached, use the `?v=3` URL or close and reopen the tab.

## Next step

Open the fresh URL on the phone and check the hero, menu, skills, projects, journey, and contact sections by scrolling. If any section is still too wide, note the phone model/browser and the section that overflows, then adjust only the relevant mobile rule in `styles.css`.
