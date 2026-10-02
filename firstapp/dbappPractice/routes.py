from flask import render_template,request
from models import Person

def register_routes(app,db):
    @app.route('/',methods=['GET'])
    def index():
        if request.method=="GET":
            people=Person.query.all()
            return render_template('index.html',people=people,message=f"1")
        
    
    @app.route('/delete/<pid>',methods=['GET'])
    def delete(pid):
        Person.query.filter(Person.pid==pid).delete()
        db.session.commit()
        people=Person.query.all()
        return render_template('index.html',people=people,message=f"1")

    @app.route('/add/<pid>',methods=['GET'])
    def add(pid):
        if pid not in Person.query.all():
            name='faisal'
            age='55'
            job='se'
            person=Person(pid=pid,name=name,age=age,job=job)
        
            db.session.add(person)
            db.session.commit()
            people=Person.query.all()
            return render_template('index.html',people=people,message=f"PID++")
        else:
            return render_template('index.html',people=people,message=f"PID Does not exists")
