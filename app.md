```python
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
res = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
data = res.json()
return f"Post id: {escape(id)} and title: {escape(data['title'])}"

# HTTP Methods

@app.get("/login")
def login_page():
return "Login Page"

@app.post("/login")
def login_check():
form = request.form
params = request.args.get('role')
return { 'username':form['username'],'password':form['password'],'params':params }

@app.route("/signup",methods=['GET','POST'])
def signup():
if(request.method == "GET"):
return "SignUp Page"
else:
return "SignUp successfully"

@app.route('/uploads',methods=['GET','POST'])
def uploadthing():
if request.method == 'POST':
file = request.files['file']
accepted_files= ['jpg','png','jpeg']

        if file:
            filename = secure_filename(file.filename)
            ext = filename.split('.')[1]
            if ext not in accepted_files:
                return f'{[ext]} Not allowed this type of file accepted files are {accepted_files}'
            file.save(f'./uploads/{filename}')
            return { 'message':"Successfully uploaded"}
        else:
            return { 'message':"There is no file to uploaded"}

@app.route('/forms',methods=['GET','POST'])
def forms():
if(request.method == "POST"):
form = request.form
return { 'skills':form.getlist('skills') ,'data':form }
else:
return render_template('forms.html')

@app.route('/json')
def json_data():
return jsonify({'error':'Hi am here oops!'})

@app.route('/dashboard/<role>')
def dashboard(role):
if role == "admin":
return "Hi admin panel is here"
elif role == "user":
return "Hi user panel is here"
else:
return redirect('/')
```
