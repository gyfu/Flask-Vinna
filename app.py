from flask import Flask, request, url_for, render_template, session, redirect, g
import urllib, json, os
app = Flask(__name__)
app.secret_key=os.urandom(24)
titlestring="Verkefni 6 - Login"

@app.route('/')
@app.route('/index')
def index():
    if g.user:
        return render_template("index.html",title=titlestring,test=session["user"])
    return render_template("index.html",title=titlestring)

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        session.pop("user", None)
        if request.form["password"]=="password":
            session['user']=request.form["user"]
            return redirect(url_for("index"))
    return render_template("login.html", title=titlestring)

@app.route('/logout')
def logout():
    referrer=request.referrer
    session.pop("user",None)
    return redirect(referrer)

@app.before_request
def before_request():
    g.user=None
    if "user" in session:
        g.user=session["user"]

@app.errorhandler(404)
def page_not_found(e):
    return "Þessi sýða fannst ekki(404 error)"





if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
#    app.run()

