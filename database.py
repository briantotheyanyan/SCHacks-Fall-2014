from pymongo import Connection
import math
import unicodedata
Connection = Connection('localhost',27017)
db=Connection.admin
res=db.authenticate('admin','pwd')
Accounts = db.Accounts
AccountsSchedules = db.AccountSchedules
GlobalSchedules = db.GlobalSchedules

#def addUserTime(username, data, hourStart, hourEnd):
    
