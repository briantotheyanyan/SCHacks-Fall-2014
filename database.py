from pymongo import Connection
import math
import unicodedata
Connection = Connection('localhost',27017)
db=Connection.admin
res=db.authenticate('admin','pwd')
Accounts = db.Accounts
AccountsSchedules = db.AccountSchedules
GlobalSchedules = db.GlobalSchedules

def verifyUser(username,password):
    if(Accounts.find({'username':username,'password':password}).count() != 0):
        return True
    return False

def addUser(username,password):
    if(verifyUser(username,password)):
       return False
    Accounts.insert({'username':username,'password':password})
    return True

def addUserTime(username, day, timeStart, timeEnd):
    if(AcountsSchedules.find({'username':username,'day':day}).count() == 0):
        a=[]
        for i in range(24):
            a.append(False)
        AccountsSchedules.insert({'username':username,'day':day,'times':times})
    currentUser = AccountsSchedules.find_one({'username':username,'day':day})['times']
    while(timeStart < timeEnd):
        currentUser[timeStart] = True
        timeStart = timeStart + 1
    AccountSchedules.update({'username':username,'day':day},{"$set":{'times':currentUser}})

def addGlobalTime(day, timeStart, timeEnd):
    if(GlobalSchedules.find({'day':day}).count() == 0):
        a=[]
        for i in range(24):
            a.append(0)
        GlobalSchedules.insert({'day':day,'times':a})
    currentDay = GlobalSchedules.find_one({'day':day})['times']
    while(timeStart < timeEnd):
        currentDay[timeStart] = currentDay[timeStart] + 1
        timeStart = timeStart + 1
    GlobalSchedules.update({'day':day}, {"$set": {'times':currentDay}})

def getDataForTime(day, timeStart):
    if(GlobalSchedules.find({"day":day}.count()) == 0):
        return 0
    currentDay = GlobalSchedules.find_one({'day':day})['times']
    return currentDay[timeStart]
