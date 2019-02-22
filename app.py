from flask import Flask, request, url_for
from flask import render_template
import urllib, json
app = Flask(__name__)
title="Miðannarverkefni"
titill="Bensín"
with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())
@app.route('/')
def main():
    listi=[]
    for x in data["results"]:
        if x["company"] in listi:
            pass
        else:
            listi.append(x["company"])
    return render_template("front.html",title=title,titill=titill,efni=listi)
@app.route('/company/<company>')
def fyrirtaekji(company):
    listi=[]
    for x in data["results"]:
        if x["company"]==company:
            listi.append(x["name"])
    lengd=len(listi)
    return render_template("content.html",title=title,titill=titill,efni=listi,company=company,num=lengd)
@app.errorhandler(404)
def page_not_found(e):
    return "Þessi sýða fannst ekki(404 error)"



if __name__ == "__main__":
#    app.run(debug=True, use_reloader=True)
    app.run()

