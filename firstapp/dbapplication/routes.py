from flask import render_template,request

from models import User
from flask_login import login_user,logout_user,current_user,login_required


def register_routes(app,db,bcrypt):
    @app.route('/',methods=['GET','POST'])
    def index():
        if current_user.is_authenticated:
            return str(current_user.username)
        else:
            return f"NO user is logged in"

    @app.route('/login/<uid>')
    def login(uid):
        user=User.query.get(uid)
        login_user(user)
        return f'Login'
    
    @app.route('/logout/')
    def logout():
        logout_user()
        return f'Logout'






































# from models import Person

# def register_routes(app,db):
#     @app.route('/',methods=['POST','GET'])
#     def index():
#         if request.method=='GET':
#             people=Person.query.all()
#             return render_template("index.html",people=people)
#         elif request.method=="POST":
#             name=request.form.get('name')
#             age=int(request.form.get('age'))
#             job=request.form.get('job')

#             person=Person(name=name,age=age,job=job)

#             db.session.add(person)
#             db.session.commit()

#             people=Person.query.all()
#             return render_template("index.html",people=people)
        

#     @app.route('/delete/<pid>',methods=['POST'])
#     def delete(pid):
#         Person.query.filter(Person.pid==pid).delete()
#         db.session.commit()
#         people=Person.query.all()
#         return render_template('index.html',people=people)
    
#     @app.route('/details/<pid>')
#     def detail(pid):
#         person=Person.query.filter(Person.pid==pid).first()
#         return render_template('detail.html',person=person)

