from flask import Flask
from model import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost/person"
db.init_app(app)
Migrate(db=db,app=app)

with app.test_request_context():
    print('Hi testing...')

if __name__ == "__main__":
    app.run(debug=True)