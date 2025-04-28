from flask import Flask,request,render_template
from markupsafe import escape
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html',name="John Doe")

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

@app.get('/posts')
def posts():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = res.json()
    return render_template('posts.html',posts=data)

@app.route("/posts/<int:id>")
def post_id(id):
    return f"Post id: {escape(id)}"


# HTTP Methods

@app.get("/login")
def login_page():
    return "Login Page"

@app.post("/login")
def login_check():
    return "Login successfully"

@app.route("/signup",methods=['GET','POST'])
def signup():
    if(request.method == "GET"):
        return "SignUp Page"
    else:
        return "SignUp successfully"

if __name__ == "__main__":
    app.run(debug=True)