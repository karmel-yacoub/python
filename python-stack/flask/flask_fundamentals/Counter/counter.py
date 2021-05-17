from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def index():
        if 'key_name' in session:
            print('key exists!')
        else:
            print("key 'key_name' does NOT exist")

        return render_template("index.html")

@app.route("/counter",methods=["post"])
def counter_show():

@app.route("/destroy",methods=["post"])
def destroy_session():
    session.clear()		
    session.pop('key_name')
    return redirect("/")		


if __name__ == "__main__":
    app.run(debug=True)
