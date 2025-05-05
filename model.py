from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))

    def to_dis(self):
        print(f' Hi id= {self.id} and name= {self.name}')