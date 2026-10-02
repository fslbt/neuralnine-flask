from flask import Flask,request,make_response
app=Flask(__name__)


@app.route('/')
def index():
    return "Hello"

#@app.route('/hello',methods=['POST','GET'])
@app.route('/hello')
def hello():
   # """if request.method=='GET':
   #     return f"You have made a GET request\n"
   # elif request.method=='POST':
   #     return f"You have made a POST request\n"
   # else:
   #     return f"You are never going to see this message\n"""
    response=make_response('Hello ')
    response.status_code=202
    response.headers['content-type']='application/octet-faisal'
    return response

    
#status code next to return return f'hello\n',201



@app.route('/hello/<name>')
def hello1(name):
    return f"hello {name}"


@app.route('/hello/<int:number1>/<int:number2>')
def hello2(number1,number2):
    return f" {number1}+{number2}={number1+number2}"

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting=request.args['greeting']
        name=request.args.get('name')
        return f"{greeting},{name}"
    else:
        return f"Some Url parameters are missing\n"


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5555,debug=True)