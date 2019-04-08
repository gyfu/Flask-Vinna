from flask import Flask, request, url_for, render_template, session, redirect, g
import urllib, json, os, sqlite3
app = Flask(__name__)
app.secret_key=os.urandom(24)
titlestring="Verkefni 6 - Login"
DATABASE="database.db"
def get_db():
    db=getattr(g,"_database",None)
    if db is None:
        db=g._database=sqlite3.connect(DATABASE)
    return db
@app.teardown_appcontext
def close_connection(exception):
    db=getattr(g,"_database",None)
    if db is not None:
        db.close()
@app.route('/')
@app.route('/index')
def index():
    c=get_db().cursor()
    c.execute("SELECT user FROM users")
    print(c.fetchone())
    if g.user:
        return render_template("index.html",title=titlestring,test=session["user"])
    return render_template("index.html",title=titlestring)
@app.route('/signup',methods=["GET","POST"])
def signup():
    c=get_db().cursor()
    if request.method=="POST":
        user=request.form["user"]
        password=request.form["password"]
        nafn=request.form["nafn"]
        listi=[(user,password,nafn)]
        c.executemany('''INSERT INTO users VALUES (?,?,?);
        ''',listi)
        get_db().commit()
        for row in c.execute("SELECT * FROM users"):
            print(row)
        print(c.fetchone())
        return redirect(url_for("svar"))
    return render_template("signup.html",title=titlestring)
@app.route('/login',methods=["GET","POST"])
def login():
    c=get_db().cursor()
    if request.method=="POST":
        test=request.form["user"]
        c.execute('''SELECT pass FROM users WHERE user=?''',(test,))
        password=c.fetchone()
        c.execute('''SELECT user FROM users WHERE user=?''',(test,))
        user=c.fetchone()
        print(password[0],user[0])
        session.pop("user", None)
        if request.form["password"]==password[0]:
            session['user']=user[0]
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
        c=get_db().cursor()
        data=[]
        for row in c.execute("SELECT * FROM users"):
            data.append(row)
        print(data)
        return render_template("svar.html",title=titlestring,listi=data)
    else: 
        return render_template("index.html",title=titlestring)
@app.before_request
def before_request():
    g.user=None
    if "user" in session:
        g.user=session["user"]
@app.errorhandler(404)
def page_not_found(e):
    return "Þessi sýða fannst ekki(404 error)"
if __name__ == "__main__":
#    app.run(debug=True, use_reloader=True)
    app.run()
