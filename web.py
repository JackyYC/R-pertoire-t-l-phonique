from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/Add')
def Add():
    return render_template("Add.html")
@app.route('/Search')
def Search():
    return render_template("Search.html")

if __name__ == '__main__':
    app.run(debug=True)