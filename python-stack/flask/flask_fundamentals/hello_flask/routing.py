from flask import Flask 
app = Flask(__name__)
@app.route('/')
def hello_world():
    print ("hello world!")
    return 'Hello World!'
@app.route('/dojo')
def print_dojo():
    print("Dojo!")
    return 'Dojo!'
@app.route('/say/<name>')
def print_hi(name):
    print("hi "+name)
    return 'hi '+name


@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    string=""
    for i in range(int(num)):
        string+="<p>"+word+"</p>"
    return string


@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again"

if __name__=="__main__":
    app.run(debug=True)