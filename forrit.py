from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title="Síða eitt", content="Lorem Síða 1.")
@app.route('/sida1')
def sida1():
    return render_template('index.html',title="Síða tvö",content="Lorem Síða 2")
@app.route('/sida2')
def sida2():
    return render_template('index.html',title="Síða þrjú",content="Lorem Síða 3")

if __name__ == "__main__":
#    app.run(debug=True, use_reloader=True)
    app.run()
