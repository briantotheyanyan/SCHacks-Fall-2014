from flask import request,Flask,render_template, url_for,redirect,request,make_response
from time import gmtime, strftime, localtime
import urllib2,json
import database
import datetime

now = datetime.datetime.now()

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
                resp = make_response(redirect(url_for('scheduleMaker')))
                resp.set_cookie('username',username)
                return resp
            return redirect(url_for('main'))
        elif request.form['button'] == "register":
            database.addUser(username,password)
            return redirect(url_for('main'))

@app.route('/scheduleMaker', methods=['GET','POST'])
def scheduleMaker():
    if request.method == 'GET':
        username = request.cookies.get('username')    
        return render_template('makeSchedule.html')
    else:
        username = request.cookies.get('username')
        if request.form["button"] == "Submit":
            month = int(request.form["month"])
            day = int(request.form["day"])
            year = int(request.form["year"])
            hour1 = int(request.form["hour1"])
            hour2 = int(request.form["hour2"])
            date = ""
            if month < 10:
                date = "0"
            date = date + str(month) + "/"
            if day < 10:
                date = date + "0"
            date = date + str(day) + "/"
            date = date + str(year)
            database.addUserTime(username,date,hour1,hour2)
            database.addGlobalTime(day,hour1,hour2)
            resp = make_response(redirect(url_for('scheduleMaker')))
            resp.set_cookie('username',username)
            return resp
        elif request.form["button"] == "See your data":
            resp = make_response(redirect(url_for('yourdata')))
            resp.set_cookie('username',username)
            return resp
        elif request.form["button"] == "See other data":
            resp = make_response(redirect(url_for('otherdata')))
            resp.set_cookie('username', username)
            return resp

@app.route('/yourdata', methods=['GET','POST'])
def yourdata():
    if request.method == 'GET':
        username = request.cookies.get('username')
        userSchedule = database.getAllUser(username)        
        times = database.arrToString(userSchedule[1])
        times = times[0:len(times)-2]
        return render_template('yourdata.html',dayList=userSchedule[0],timeList=times)
    elif request.form["button"] == "Go Back":
        resp = make_response(redirect(url_for('scheduleMaker')))
        resp.set_cookie('username',username)
        return resp

@app.route('/otherdata', methods=['GET','POST'])
def otherdata():
    if request.method == 'GET':
        username = request.cookies.get('username')
        return render_template('otherdata.html')
    elif(request.form["button"] == "Go Back"):
        resp = make_response(redirect(url_for('scheduleMaker')))
        resp.set_cookie('username',username)
        return resp    

if __name__=="__main__":
    app.debug=True
    app.run(port=5000)
