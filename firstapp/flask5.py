from flask import Flask,render_template

app=Flask(__name__,template_folder="templates",static_folder="static",static_url_path="/")

@app.route('/')
def index():
    cat="i love cats"
    return render_template('other4.html',cat=cat)
@app.template_filter('reverse_string')
def reversestring(n):
    a=n[::-1]
    return a


if __name__=="__main__":
    app.run("0.0.0.0",port=5554,debug=True)