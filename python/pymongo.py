__author__ = 'xyz'
from pymongo import MongoClient
focusid='123456'

client=MongoClient('servername',8080)
db=client.ox
clen=db.file
DeliverStatus=clen.find_one({"cusid": cusid})
print "focusid:" +focusid
if str(DeliverStatus).find("u'status': u'COMPLETE'"):
    DeliverStatus=str(DeliverStatus)[2:23]
else: DeliverStatus='None'
print DeliverStatus
