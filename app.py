from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    """Render the cafe landing page."""
    return render_template("index.html", page_title="Café Kouis | Home")


@app.get("/about")
def about():
    """Render a page describing the prototype and its purpose."""
    return render_template("about.html", page_title="Café Kouis | About")


if __name__ == "__main__":
    app.run(debug=True)
