"""Flask-приложение с шаблоном Jinja2."""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index() -> str:
    """Рендерит шаблон с данными."""
    user = {
        "name": "Екатерина",
        "items": ["Python", "Flask", "Jinja2"],
    }
    return render_template("index.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)