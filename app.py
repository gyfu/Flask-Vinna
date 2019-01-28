from flask import Flask, request, url_for
from flask import render_template
app = Flask(__name__)
frettir=[
        ["Banaslys á sjó","Lorem Ipsum","htj@htj.is"],
        ["Fiskveiðifrétt","Lorem Ipsum","bb@bb.is"],
        ["Stríð í Gaza","Lorem Ipsum","frs@frs.com"],
        ["Kína er að gera eitthvað, ég veit ekki","Lorem Ipsum","cnn@cnn.is"]
        ]
@app.route('/')
def main():
    return render_template("base.html",title="Verkefni3 - Fréttir")
@app.route('/frett/<int:num>')
def frettir(num):
    return str(num)
@app.errorhandler(404)
def page_not_found(e):
    return "Þessi sýða fannst ekki(404 error)"



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
#    app.run()

