# EGN475 W1A1 Personal-Explanation Drafts

> **Use responsibly:** The assignment’s exact question text was not provided. These are preparation drafts for common setup-and-prototype questions, not a claim about the instructor’s wording. Read the code, test it yourself, and rewrite each answer in your own voice so it accurately describes your own work.

## Draft 1 — Why use a virtual environment?

**Question:** Why is a Python virtual environment useful for this project?

**Draft answer:** A virtual environment keeps this project’s Python packages separate from packages installed for other projects. In this project, Flask is installed inside the `.venv` folder, so the application can use the version listed in `requirements.txt` without changing the system-wide Python installation. This makes the setup more repeatable because another developer can create a new `.venv` and install the same project requirements.

## Draft 2 — What is the purpose of `.gitignore`?

**Question:** What does the `.gitignore` file do in this repository?

**Draft answer:** The `.gitignore` file tells Git not to track files that are generated locally or that do not belong in the source repository. Here, it excludes `.venv/`, where the local virtual environment stores installed packages, and `__pycache__/`, where Python stores compiled cache files. Ignoring those folders keeps commits focused on source code and avoids adding machine-specific or automatically generated files.

## Draft 3 — How do the Flask routes work?

**Question:** Explain what happens when someone visits `/` or `/about`.

**Draft answer:** Flask uses decorators above Python functions to associate each URL with a route. The `@app.get("/")` decorator maps the home URL to the `home()` function, while `@app.get("/about")` maps the about URL to `about()`. Each function calls `render_template`, which loads the matching HTML file from the `templates` folder and sends it back to the browser as the response.

## Draft 4 — Why make separate Git commits?

**Question:** Why were changes divided into separate Git commits?

**Draft answer:** Separate commits create a readable development history. The first commit establishes the basic Flask setup and home page, the second adds the about-page feature, and the third adds tests and documentation. This makes it easier to review what changed at each stage, return to an earlier version if a problem occurs, and show that the prototype developed in meaningful steps instead of appearing as one unexplained final upload.
