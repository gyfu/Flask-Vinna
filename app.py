from flask import Flask, request, url_for, render_template
from flask_wtf import Form
from wtform import StringField, PasswordField
from wtform.validators import DataRequired, Email
import urllib, json
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def main():
    return render_template("content.html", title="Verkefni 5 - Forms")
@app.errorhandler(404)
def page_not_found(e):
    return "Þessi sýða fannst ekki(404 error)"



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
#    app.run()

