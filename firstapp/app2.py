from flask import Flask,request,make_response
app=Flask(__name__)

@app.route('/')
def hel():
    return("What are we doing\n")

@app.route('/temp',methods=['POST'])
def nue():
    return f"new route\n"

@app.route('/hello/<int:n1>/<int:n2>') #Url procesors
def add(n1,n2):
    return f"{n1}+{n2}={n1+n2}"

@app.route('/hello')
def handleurl():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting=request.args['greeting']
        name=request.args.get('name')
        return f"{name} says {greeting}"
    else:
        return f"You are missing some url parameters"

@app.route('/custom',methods=['GET'])
def custom():
    response=make_response('Hello')
    response.status_code=202
    response.headers['content-type']="faisal"
    return response




if __name__=='__main__':
    app.run(host='0.0.0.0',port=5555,debug=True)