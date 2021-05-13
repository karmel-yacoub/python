from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    x=3
    color="aqua"
    return render_template("index.html",x=x,color="aqua")

@app.route('/play/<x>')
def index2(x):
    color="aqua"
    return render_template("index.html",x=int(x),color="aqua")

@app.route('/play/<x>/<color>')
def index3(x,color):
    return render_template("index.html",x=int(x),color=color)

    	
if __name__=="__main__":
    app.run(debug=True)
