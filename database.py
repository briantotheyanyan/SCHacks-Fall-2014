from pymongo import Connection
import math
import unicodedata
Connection = Connection('localhost',27017)
db=Connection.admin
res=db.authenticate('admin','pwd')
Accounts = db.Accounts
AccountsSchedules = db.AccountSchedules
GlobalSchedules = db.GlobalSchedules
databases = [Accounts,AccountsSchedules,GlobalSchedules]
def verifyUser(username,password):
    if(Accounts.find({'username':username,'password':password}).count() != 0):
        return True
    return False

def addUser(username,password):
    if(verifyUser(username,password)):
       return False
    Accounts.insert({'username':username,'password':password,'times':[]})
    return True

def addUserTime(username, day, timeStart, timeEnd):
    if(AccountsSchedules.find({'username':username,'day':day}).count() == 0):
        a=[]
        for i in range(24):
            a.append(False)
        AccountsSchedules.insert({'username':username,'day':day,'times':a})
    currentUser = AccountsSchedules.find_one({'username':username,'day':day})['times']
    while(timeStart < timeEnd):
        currentUser[timeStart] = True
        timeStart = timeStart + 1
    AccountsSchedules.update({'username':username,'day':day},{"$set":{'times':currentUser}})

def getAllUser(username):
    alluser = AccountsSchedules.find({'username':username})
    schedulesbyUser = []
    for x in alluser:
        schedulesbyUser.append([str(x['day']).encode('ascii','ignore'),int(x['time'])])

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

def getGlobalDataForTime(day, timeStart):
    if(GlobalSchedules.find({"day":day}).count() == 0):
        return 0
    currentDay = GlobalSchedules.find_one({'day':day})['times']
    return currentDay[timeStart]

def getUserDataForTime(username, day, startTime):
    if(AccountsSchedules.find({'username':username,'day':day}).count() == 0):
        return 0
    current = AccountsSchedules.find_one({'username':username,'day':day})['times']
    return current[startTime]

def clearDatabases():
    for x in databases:
        x.drop()

#clearDatabases()
