from flask import Flask,request,make_response,render_template,redirect,url_for

app=Flask(__name__,template_folder='templates')

@app.route('/',methods=['GET','POST']) #Request Methods
def index():
    return f"hello world"

@app.route('/home/<name>') #Url Processors
def home(name):
    return f"this is home of {name}"

@app.route('/math/<int:n1>/<int:n2>')
def math(n1,n2):
    return f"sum is {n1}+{n2}={n1+n2}"

@app.route('/greeting')# Url Parameters
def greeting():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting=request.args["greeting"]
        name=request.args.get('name')
        return f"{name} says {greeting}"

@app.route('/custom') #CUSTOM RESPONSE
def custom():
    response=make_response('hello')
    response.status_code=123
    response.headers['content-type']='faisal'
    return response

@app.route('/render')
def render():
    myval=[1,2,3,4,5]
    return render_template('index4.html',myval=myval)

@app.route('/template')
def template():
    cat="I love cats"
    myval=[1,2,3,4,5]
    return render_template("index4.html",cat=cat,myval=myval)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.route('/redirect')
def redirect_route():
    return redirect(url_for('other4'))


@app.route('/other4')
def other4():
    cat = "I love cats"
    return render_template("other4.html", cat=cat)
if __name__=='__main__':
    app.run(host="0.0.0.0",port=5555,debug=True)