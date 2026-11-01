# EGN475 Café Kouis Flask Prototype

A small Flask prototype with a home page and an about page. It demonstrates the basic request-to-response flow: Flask receives a URL request, runs the matching route function, and returns an HTML template.

## Routes

| Route | Purpose |
| --- | --- |
| `/` | Café Kouis home page |
| `/about` | Explanation of the prototype's organization |

## Project structure

```text
app.py                 Flask application and route functions
templates/             HTML templates returned by the routes
static/style.css       Shared stylesheet
tests/test_app.py      Automated route tests
requirements.txt       Python dependencies
.gitignore             Excludes .venv/ and __pycache__/
```

## Run on Windows (PowerShell)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
flask --app app run --debug
```

Then open `http://127.0.0.1:5000/` and `http://127.0.0.1:5000/about` in a browser.

## Run the tests

With the virtual environment active:

```powershell
python -m unittest discover -s tests -v
```

## Academic-use note

The repository includes automated-assistance disclosure files. Review the code and rewrite the personal-response drafts in your own words before submitting course work. The technical claims in a final submission should match the environment and actions you personally verified.
