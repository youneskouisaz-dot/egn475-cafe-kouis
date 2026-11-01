# Truthful Assistance and Evidence Log

**Assignment materials:** EGN475 Flask prototype, Café Kouis  
**Log date:** 2026-11-01  
**Purpose:** Record what Manus actually did, distinguish it from student actions, and avoid presenting generated drafts or automated work as the student's own work.

## User request

The user requested a Flask prototype with `/` and `/about`, a virtual environment, Git ignore rules, at least three meaningful Git commits, real testing evidence, report materials, and a public GitHub repository named `egn475-cafe-kouis`.

## Assistance and verification actually performed

1. Created the working project in the Manus Ubuntu sandbox at `/home/ubuntu/egn475-cafe-kouis`.
2. Created a Python virtual environment with the sandbox's Python 3.12.3 and installed Flask 3.1.3. This is not the user's Windows environment; `.venv/` is excluded from Git.
3. Wrote the Flask application, templates, stylesheet, route tests, README, four explanation drafts, interaction log, and report draft.
4. Added `.venv/` and `__pycache__/` to `.gitignore` and verified the ignore behavior.
5. Tested the home and about routes with Flask's test client, ran four automated `unittest` cases, and checked both routes over HTTP. Captured actual Chromium browser images of `/` and `/about` in `browser-home.png` and `browser-about.png` (also stored in the local `evidence/` folder).
6. Created a separate local Git history in the sandbox using the transparent automated-assistance identity `Manus Coursework Assistant <dev-agent@manus.ai>`. This local history was **not** pushed to GitHub.
7. After the user logged into GitHub in the browser, created the requested **public** repository using GitHub's signed-in web interface and uploaded the source and materials. GitHub's normal web upload/editor created five core project commits on `main`, attributed by GitHub to the signed-in account `youneskouisaz-dot`:
   - `42a0666` — `Create README.md`
   - `af5cd28` — `Add Flask source and assignment evidence`
   - `70b9fe4` — `Add home and about page templates`
   - `a8e7b6e` — `Add shared cafe page styling`
   - `135c5bc` — `Add automated Flask route tests`
   Later documentation/README maintenance commits include `06b76c2` (`Update verified report and AI log`) and `91e91c3` (`Improve README project structure and setup guide`). This log and the PDF were refreshed and uploaded again after those commits; that further documentation update is also visible in the live history. The GitHub commit page is the source of truth for the complete sequence.
8. Verified the public repository and its file tree through GitHub, cloned it over HTTPS into a temporary directory, ran the uploaded tests against that clone (4 tests passed), and confirmed `/` and `/about` both returned HTTP 200. The public repository is <https://github.com/youneskouisaz-dot/egn475-cafe-kouis>.

## Important attribution and environment distinctions

- Although the GitHub web commits are genuine commits created through GitHub's signed-in interface, they are attributed to the user's logged-in GitHub account. Manus prepared/uploaded the files and submitted the commit actions. Do not claim that the student personally authored or typed these changes; disclose assistance as required by the course.
- The public GitHub commit history is separate from the sandbox's local Git history; the local history was not pushed. The five core project commits listed above satisfy the three-commit requirement. Later report and README maintenance commits are also present; the live GitHub history shows the full sequence.
- The Python virtual environment and execution environment used for verification are in the Manus Ubuntu sandbox. The user still needs to create and run a virtual environment on their Windows 11 computer if the assignment expects local-machine evidence.
- No Windows desktop or VS Code was accessed. No authentic VS Code screenshot is included.
- GitHub Copilot Chat was not accessed. No Copilot interaction, output, or screenshot is claimed.
- No instructor-supplied assignment sheet or pre-existing student screenshot was available in the sandbox. The four answer drafts may not match the assignment's exact questions.

## Student follow-up

Before submission, the student should read and understand the source, independently create/run the project in the required Windows environment, rewrite the four personal-explanation drafts in the student's own words using the actual assignment questions, capture authentic VS Code evidence if required, and follow the course policy for disclosing or citing AI assistance. Do not submit the drafts unchanged as personal explanations.
