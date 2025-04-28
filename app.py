from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def syHi():
    return "Hi from flask"

@app.route("/welcome")
def welcome():
    return "<h1>Welcome flask server</h1>"

@app.route("/name/<name>")
def name(name:str):
    return f"Hi {escape(name)} welcome"

if __name__ == "__main__":
    app.run(debug=True)