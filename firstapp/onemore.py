from flask import Flask,request,make_response,render_template,url_for,redirect

app=Flask(__name__,template_folder='templates')

@app.route('/')
def hello():
    return f"hello"

@app.route('/makeres')
def makeres():
    response=make_response('hello')
    response.status='201'
    response.headers['Content-Type']="faisal"
    return response

@app.route('/bye/<int:c1>/<int:c2>')
def bye(c1,c2):
    return f"{c1}+{c2}={c1+c2}"

@app.route('/req',methods=['POST'])
def req():
    return f'POST'

@app.route('/makereq')
def makereq():
    if 'name' in request.args.keys() and 'greeting' in request.args.keys():
        name=request.args['name']
        greeting=request.args.get('greeting')
        return f'{name},{greeting}'

@app.route('/simpletemplate')
def simpletemplate():
    name="faisal"
    cars=[1,2,3,4,5,6]
    age=26
    return render_template('onemore.html',name=name,cars=cars,age=age)
@app.template_filter('reverse')
def reverse(n):
    a=n[::-1]
    return a
@app.route('/redirect')
def redirecting():
    return redirect(url_for('other4'))

@app.route('/other4')
def other4():
    cat="i love cats"
    return render_template("other4.html",cat=cat)

@app.template_filter("reverse_string")
def reverse_string(n):
    a=n[::-1]
    return a

if __name__=="__main__":
    app.run("0.0.0.0",port=5555,debug=True)