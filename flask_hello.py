"""Flask-приложение «Hello World»."""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello() -> str:
    """Возвращает приветствие."""
    return "Привет Flask!"

if __name__ == "__main__":
    app.run(debug=True)