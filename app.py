from flask import Flask, render_template, request

app = Flask(__name__)

global listContact
listContact = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Add')
def Add():
    return render_template("Add.html")

@app.route('/EndAdd', methods = ['POST'])
def EndAdd():
    contact = request.form
    listContact.append(contact)
    return render_template("EndAdd.html")

@app.route('/Search')
def Search():
    return render_template("Search.html")

@app.route('/EndSearch', methods = ['POST'])
def EndSearch():
    searching = request.form
    sn = searching["name"]
    for i in range (len(listContact)):
        if listContact[i]["name"] == searching["name"] :
            n = listContact[i]["name"]
            num = listContact[i]["number"]
            return render_template("EndSearch.html", name = n, number = num)
    return render_template("NotFound.html", name = sn)

if __name__ == '__main__':
    app.run(debug=True)