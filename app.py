from flask import Flask, request, url_for, render_template, session, redirect, g
import urllib, json, os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app.db"
app.secret_key=os.urandom(24)
titlestring="Verkefni 7 - Login/MySQL"

db=SQLAlchemy(app)


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
        if request.form["password"]=="password" and request.form["user"]=="admin":
            session['user']=request.form["user"]
            return redirect(url_for("svar"))
    return render_template("login.html", title=titlestring)

@app.route('/logout')
def logout():
    referrer=request.referrer
    session.pop("user",None)
    return redirect(referrer)
@app.route('/svar')
def svar():
    if g.user:
        string="Cookie er data sem server sendir client sem geymir upplýsingar um client-in og það sem hann gerir. Session er tímabilið sem client er í þegar hann er t.d. loggaður inn á vefsíðu. Cache er upplýsingasafn á vafra hjá notanda"
        return render_template("svar.html", efni=string)
    return render_template("svar.html",efni="Þú hefur ekki aðgang að þessari síðu")

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

