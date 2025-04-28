from flask import Flask

app = Flask(__name__)


@app.route("/")
def syHi():
    return "Hi from flask"


if __name__ == "__main__":
    app.run(debug=True)