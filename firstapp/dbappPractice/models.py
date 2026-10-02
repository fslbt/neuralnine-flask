from app import db


class Person(db.Model):
    __tablename__='people'
    pid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    job=db.Column(db.Text)

    def __repr__(self):
        return f"Pid :{self.pid} Name: {self.name} \n Age: {self.age} \n Job:{self.job}"
    
