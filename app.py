from flask import request,Flask,render_template, url_for,redirect,request,make_response
from time import gmtime, strftime, localtime
import urllib2,json
import database


app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods=['GET','POST'])
def main():
    if(request.method == 'GET'):
        return render_template("home.html")
    else:
        username = request.form['username']
        password = request.form['password']
        if request.form['button'] == "login":
            if(database.verifyUser(username,password)):
                return redirect(url_for('success'))
            return redirect(url_for('failure'))
        elif request.form['button'] == "register":
            database.addUser(username,password)
            return redirect(url_for('main'))

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
