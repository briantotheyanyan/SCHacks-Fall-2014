from flask import request,Flask,render_template, url_for,redirect,request,make_response
from time import gmtime, strftime, localtime
import urllib2,json
import database


app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods=['GET','POST'])
def main():
    if(request.method == 'POST'):
        if request.form['submit'] == 'login':
            if(database.verifyUser(request.form['username'],request.form['password'])):
                return redirect(url_for("/success"))
            else:
                return redirect(url_for("/failure"))
        elif request.form["submit"] == 'register':
            database.addUser(request.form['username'],request.form['password'])
    else:
        return render_template("home.html")
@app.route('/success', methods=['GET','POST'])
def success():
    if request.method == 'GET':
        return render_template('success.html')
    return

@app.route('/failure', methods=['GET','POST'])
def failure():
    if request.method == 'GET':
        return render_template('failure.html')
    return

if __name__=="__main__":
    app.debug=True
    app.run(port=5000)
