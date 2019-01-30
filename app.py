from flask import Flask, request, url_for
from flask import render_template
import urllib, json
app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/currency/m5") as url:
    data = json.loads(url.read().decode())
    test=data["results"][0]["longName"]
@app.route('/')
def main():
    return render_template("content.html",title="Verkefni4 - API", titill="API verkefni", efni=data["results"])
@app.errorhandler(404)
def page_not_found(e):
    return "Þessi sýða fannst ekki(404 error)"



if __name__ == "__main__":
#    app.run(debug=True, use_reloader=True)
    app.run()

