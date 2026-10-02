from flask import Flask,render_template,redirect,url_for
app=Flask(__name__,template_folder='templates')

@app.route('/')
def greeting():
    myval="Faisal"
    myresult=10+20
    mylist=[1,2,3,4,5]
    return render_template('index.html',myval=myval,myresult=myresult,mylist=mylist)

@app.route('/filters')
def other():
    pet="cat"
    return render_template('other.html',pet=pet)

@app.route('/redirect')
def redirect_endpoint():
    return redirect(url_for('other'))


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s,times=2):
    return s*times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i%2==0 else c.lower() for i,c in enumerate(s)])



if __name__=='__main__':
    app.run(host='0.0.0.0',port=5556,debug=True)