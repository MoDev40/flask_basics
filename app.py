from flask import Flask

app = Flask(__name__)


@app.route("/")
def syHi():
    return "Hi from flask"

@app.route("/welcome")
def welcome():
    return "<h1>Welcome flask server</h1>"
if __name__ == "__main__":
    app.run(debug=True)