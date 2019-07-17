from pymongo import MongoClient


client = MongoClient('localhost:27017')
db = client['NSE1']
coll_inform = db['company_inform']
coll_data=db['company_info']

for idx in coll_inform.find():


    for jdx in coll_data.find():
        if (idx['SYMBOL']== jdx['SYMBOL'] and idx[' SERIES']==jdx[' SERIES']):

            object_id= jdx["_id"]

            db.coll_inform.update(object_id)
        else:
            continue







