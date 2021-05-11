from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def level1():
    return render_template('index.html',num_row=8,num_col=8)

@app.route('/<int:x1>')
def level2(x1):
    return render_template('index.html',num_row=x1 , num_col=8 )

@app.route('/<int:x1>/<int:y1>')
def level3(x1,y1):
    return render_template('index.html',num_row=x1 , num_col=y1 )

@app.route('/<int:x1>/<int:y1>/<color1>/<color2>')
def level4(x1,y1, color1 , color2):
    return render_template('index.html',num_row=x1 , num_col=y1 , color1 = color1 , color2 = color2  )





   
if __name__=="__main__":
    app.run(debug=True)
