from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/<x>")
def home(x):
    return f"Hello!{x}"

@app.route("/admin")
def admin():
    return render_template("home.html",content="weqwe")

if __name__=="__main__":
    app.run(debug=True)