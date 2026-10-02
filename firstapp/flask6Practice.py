from flask import Flask,render_template,session,make_response,request

app=Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/')

@app.route('/')
def index():
    return f'hello'

app.secret_key='key'
@app.route('/setcookie')
def setcookie():
    response=make_response(render_template('flask6P.html',message=f"Cookie Set"))
    response.set_cookie('cookie_name','cookie_value')
    return response

@app.route('/getcookie')
def getcookie():
    if 'cookie_name' in request.cookies.keys(): 
        cookie_value=request.cookies['cookie_name']
    #cookie_value=request.cookies.get('cookie_name')

        return render_template('flask6P.html',message=f"Cookie Value: {cookie_value} ",cat='i love cats')
    
    else:
        return render_template('flask6P.html',message=f"No Cookies",cat='i love cats')






@app.route('/clearcookie')
def clearcookie():
    response=make_response(render_template('flask6P.html',message=f"Cookie Clear",cat="i love cats"))
    response.set_cookie("cookie_name",expires=0)
    return response


@app.route('/setsession')
def setsession():
    session['name']='faisal'
    session['other']='Salam'
    return render_template('flask6P.html',message=f"Session Set",cat='i love cats')

    

@app.route('/getsession')
def getsession():
    if 'name' in session.keys() and 'other' in session.keys():
        name=session.get('name')
        other=session.get('other')
        return render_template('flask6P.html',message=f"Name:{name},Other:{other}",cat="i love cats")
    else:
        return render_template('flask6P.html',message=f"No Session",cat="i love cats")
    
    


@app.route('/clearsession')
def clearsession():
    session.clear()
    return render_template('flask6P.html',message=f"Session Cleared",cat="i love cats")

if __name__=="__main__":
    app.run("0.0.0.0",port=5555,debug=True)


