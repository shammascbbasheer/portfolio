from pathlib import Path


ROOT = Path(__file__).parent
required_files = ["index.html", "styles.css", "script.js", "README.md", "assets/instagram-logo.svg", "assets/linkedin-logo.svg", "assets/Shammas_CB_Resume.pdf", "assets/fathah-reference.mp4", "assets/resume-analyser.svg", "assets/ai-home-brain.svg", "assets/llm-project.svg", "assets/skill-ai-ml.svg", "assets/skill-backend.svg", "assets/skill-frontend.svg", "assets/skill-data-nlp.svg", "assets/skill-tools.svg", "assets/group-programming-web.svg", "assets/group-ai-data.svg", "assets/group-tools-collaboration.svg", "assets/group-professional-strengths.svg", "assets/journey-internship.svg", "assets/journey-education.svg", "assets/journey-certification.svg", "assets/journey-learning.svg", "assets/favicon.svg", "assets/favicon-32x32.png", "assets/favicon.ico", "assets/apple-touch-icon.png"]
for filename in required_files:
    path = ROOT / filename
    if not path.is_file() or path.stat().st_size == 0:
        raise SystemExit(f"Missing required file: {filename}")

html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "styles.css").read_text(encoding="utf-8")
js = (ROOT / "script.js").read_text(encoding="utf-8")
checks = {
    "page title": "<title>Shammas CB — Software Developer & AI/ML Portfolio</title>" in html,
    "favicon metadata": all(reference in html for reference in ('href="assets/favicon.svg"', 'href="assets/favicon-32x32.png"', 'href="assets/favicon.ico"', 'href="assets/apple-touch-icon.png"')) and "type=\"image/svg+xml\"" in html and "type=\"image/png\"" in html,
    "favicon branding": "SCB portfolio favicon" in (ROOT / "assets/favicon.svg").read_text(encoding="utf-8"),
    "hero heading": "Hi, I'm <span>Shammas CB</span>" in html,
    "projects section": 'id="projects"' in html,
    "contact form": 'id="contact-form"' in html,
    "about profile": "BCA Graduate transitioning into AI/ML engineering" in html and "entry-level AI/ML Engineer role" in html,
    "internship experience": "Artificial Intelligence Intern" in html and "Codec Technologies" in html and "Apr 2026" in html,
    "web development focus": "Back-End Web Development" in html and "Front-End Development" in html,
    "bca education": 'class="education-details"' in html and "BCA" in html and "Bachelor of Computer Applications" in html and "Harsha Institute of Management Studies" in html and "Bangalore University" in html and "Aug 2023" in html and "Problem Solving" in html,
    "ai certification": "Codec Technologies India" in html and "Issued Apr 2026" in html and "Expired May 2026" in html,
    "resume analyser project": "Resume Analyser" in html and "AI-powered Resume Analyser" in html and "Scikit-learn" in html and "Contributors: Abdul" in html,
    "resume analyser live demo": "https://resumeai-analyser.vercel.app" in html and "View live demo" in html,
    "skills profile": "Teamwork" in html and "Python (Programming Language)" in html and "React.js" in html and "Artificial Intelligence (AI)" in html,
    "structured skills directory": 'class="skills-directory' in html and "Programming &amp; web" in html and "Professional strengths" in html,
    "language profile": "Professional working proficiency" in html and "Native or bilingual proficiency" in html and "Elementary proficiency" in html,
    "professional navigation": "linkedin.com/in/shammas-cb/" in html and 'class="nav-linkedin"' in html,
    "professional project layout": "Selected projects" in html and 'class="project-card project-resume' in html,
    "premium project visuals": all(asset in html for asset in ("assets/resume-analyser.svg", "assets/ai-home-brain.svg", "assets/llm-project.svg")) and "project-visual-image" in html,
    "premium toolkit visuals": all(asset in html for asset in ("assets/skill-ai-ml.svg", "assets/skill-backend.svg", "assets/skill-frontend.svg", "assets/skill-data-nlp.svg", "assets/skill-tools.svg")) and html.count('class="skill-visual"') == 5,
    "premium skills directory visuals": all(asset in html for asset in ("assets/group-programming-web.svg", "assets/group-ai-data.svg", "assets/group-tools-collaboration.svg", "assets/group-professional-strengths.svg")) and html.count('class="skills-group-visual"') == 4,
    "premium journey visuals": all(asset in html for asset in ("assets/journey-internship.svg", "assets/journey-education.svg", "assets/journey-certification.svg", "assets/journey-learning.svg")) and html.count('class="timeline-visual"') == 4,
    "portfolio project removed": "Personal Portfolio Website" not in html and 'class="project-card project-portfolio' not in html,
    "upcoming project status": 'class="upcoming-projects"' in html and "Upcoming project" in html and "This project is not completed yet" in html,
    "llm upcoming project": "LLM Project" in html and "large language models" in html and "LLMs" in html,
    "ai home brain team": 'class="project-team"' in html and "Shammas" in html and "Project Creator" in html and "Fathah" in html and "Project Contributor" in html and "https://linkedin.com/in/abdulfathah-mj" in html and "mailto:abdulfathahmj85@gmail.com" in html,
    "direct contact details": 'href="tel:7306158143"' in html and 'href="mailto:shammascb41@gmail.com"' in html,
    "github profile": "github.com/shammascbbasheer" in html,
    "linkedin profile": "linkedin.com/in/shammas-cb/" in html,
    "resume PDF link": html.count('href="assets/Shammas_CB_Resume.pdf"') == 3,
    "video-only hero with voice control": 'class="presenter-video"' in html and 'src="assets/fathah-reference.mp4"' in html and 'class="video-voice-button"' in html and 'id="presenter-video"' in html and ' muted' in html and "class=\"presenter-image\"" not in html and "class=\"floating-note" not in html and "class=\"terminal-card" not in html,
    "instagram profile": "instagram.com/shammas_bin_basheer/" in html and "footer-instagram" in html,
    "footer social links": 'class="footer-social"' in html and "footer-instagram" in html and "footer-linkedin" in html and "footer-github" in html,
    "footer Instagram logo asset": 'src="assets/instagram-logo.svg"' in html and "Instagram camera logo" in (ROOT / "assets/instagram-logo.svg").read_text(encoding="utf-8"),
    "footer LinkedIn logo asset": 'src="assets/linkedin-logo.svg"' in html and "LinkedIn logo" in (ROOT / "assets/linkedin-logo.svg").read_text(encoding="utf-8"),
    "footer contact links": 'class="footer-contact"' in html and "7306158143" in html and "shammascb41@gmail.com" in html,
    "responsive viewport": 'name="viewport"' in html,
    "bootstrap responsive grid": "bootstrap@5.3.3/dist/css/bootstrap.min.css" in html and "col-12 col-xl-7" in html,
    "tablet breakpoint": "@media (max-width: 1100px)" in css,
    "mobile width guard": "html { width: 100%; max-width: 100%;" in css and ".hero, .hero.row { width: calc(100% - 36px);" in css,
    "touch-device fallback": "(pointer: coarse) and (max-width: 1100px)" in css,
    "mobile overflow protection": "overflow-y: auto" in css and "safe-area-inset-bottom" in css,
    "responsive menu reset": "matchMedia('(max-width: 700px)')" in js and "closeMenu()" in js,
    "voice interaction": "presenterVideo.muted = voiceEnabled" in js and "presenterVideo.play()" in js,
}
failed = [name for name, passed in checks.items() if not passed]
if failed:
    raise SystemExit("Site checks failed: " + ", ".join(failed))

print(f"Site checks passed ({len(required_files)} files, {len(checks)} content checks).")
