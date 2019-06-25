import json
from pymongo import MongoClient
from pymongo import *
from pymongo import ReadPreference
client = MongoClient('localhost:27017')
db = client['NSE1']
coll = db['TEST5']
"""
with open('csvjson.json') as data_obj:
    db_data = json.load(data_obj)

db.TEST1.insert_many(db_data)


q = {"SYMBOL": "20MICRONS"}
d = db.TEST1.find({"SYMBOL": "20MICRONS"})
k = db.TEST1.count_documents({})
print(k)

for x in d:
    print(x)

l = db.Test1.find({"SYMBOL": "DHFL", "SERIES":"EQ"})
"""

#Cur = db.TEST2.find({ '$and' : [{"SYMBOL": 1} , {"SERIES" : 1}]})

Cur = db.TEST2.find({},{'SYMBOL':1,'SERIES':1})
for i in Cur:
    db.coll.insert(Cur)

#for idx in Cur:
 #   print(idx)

