__author__ = 'sjira'
from pymongo import MongoClient
focusid='582898'

client=MongoClient('mongo.qa.mse-esp.com',8080)
db=client.esp
clen=db.cso
DeliverStatus=clen.find_one({"focusid": focusid})
print "focusid:" +focusid
if str(DeliverStatus).find("u'status': u'COMPLETE'"):
    DeliverStatus=str(DeliverStatus)[2:23]
else: DeliverStatus='None'
print DeliverStatus
