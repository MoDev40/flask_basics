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
def name(name):
    return f"Hi {escape(name)} welcome"

# Prams Variable Rules and Format
@app.route("/profile/<username>")
def profile(username):
    return f"Username: {escape(username)}"

@app.route("/posts/<int:id>")
def post_id(id):
    return f"Post id: {escape(id)}"



if __name__ == "__main__":
    app.run(debug=True)