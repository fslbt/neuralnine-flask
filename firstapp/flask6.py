from flask import Flask,render_template,session,make_response,request

app=Flask(__name__,template_folder="templates",static_folder="static",static_url_path="/")

app.secret_key='SOME KEY'


@app.route('/')
def index():
    cat="i love cats"
    return render_template('other4.html',cat=cat,message='Index')
@app.template_filter('reverse_string')
def reversestring(n):
    a=n[::-1]
    return a


@app.route('/set_data')
def set_data():
    cat='i love'
    session['name']='Faisal'
    session['other']='Hello'
    return render_template('other4.html',cat=cat,message='Session Data Set')


@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name=session['name']
        other=session['other']
        return render_template('other4.html',cat='i love',message=f'Name: {name} Other: {other}')
    else:
        return render_template('other4.html',cat='i love',message='No Session Data')

@app.route('/clear_session')
def clear_session():
    #session.pop('name')
    session.clear()
    return render_template('other4.html',cat='cat',message='Session Cleared')

@app.route('/set_cookie')
def set_cookie():
    response=make_response(render_template('other4.html',cat='cat',message='Cookie set'))
    response.set_cookie('cookie_name','cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value=request.cookies['cookie_name']
    return render_template('other4.html',cat='i love',message=f'Cookie: {cookie_value}')


@app.route('/remove_cookie')
def remove_cookie():
    response=make_response(render_template('other4.html',cat='cat',message='Cookie removed'))
    response.set_cookie('cookie_name',expires=0)
    return response




if __name__=="__main__":
    app.run("0.0.0.0",port=5554,debug=True)