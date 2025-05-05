from flask import Flask
from model import db,Person
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost/person"
db.init_app(app)
Migrate(db=db,app=app)

def add():
    new_person = Person(name="John doe")
    db.session.add(new_person)
    db.session.commit()

def readAll():
    data = Person.query.all()
    return [ x.to_dis() for x in data ]

def addMany():
    data = [ Person(name="Alai"),Person(name="Sundus")]
    db.session.add_all(data)
    db.session.commit()
    return 1

def readByName(name):
    data = Person.query.where(Person.name == name).one()
    print(data.to_dis())

with app.test_request_context():
    readByName("Alai")
    print('Hi testing...')

if __name__ == "__main__":
    app.run(debug=True)