# EGN475 Café Kouis Flask Prototype



A small Flask project demonstrating two routes: `/` for the café home page and `/about` for a description of the prototype.



## Run on Windows (PowerShell)



```powershell

py -3.12 -m venv .venv

.\.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt

flask --app app run --debug

```



Open `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/about`.



## Tests



With the virtual environment active, run:



```powershell

python -m unittest discover -s tests -v

```



Review the source and rewrite the personal explanation drafts in your own words before course submission. See `AI_INTERACTION_LOG.md` for an accurate record of assistance and evidence.
