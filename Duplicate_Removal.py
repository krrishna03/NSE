from connection import connect

db=connect()
coll = db['company_inform']
"""
for doc in coll.find():
    coll.update("and",
        { "_id": doc["_id"] },
        { "$set":{"SYMBOL":doc["SYMBOL"], " SERIES":doc[" SERIES"]} },
        upsert=True
    )
"""

db.coll.aggregate([{"$sort": {"_id": 1}},
                         {
                             "$group": {
                                 "_id": {"_id":"$_id", "SYMBOL": "$SYMBOL", " SERIES": "$ SERIES" },
                                 "doc": { "$first": "$$ROOT" }
                             }
                         },
                         { "$replaceRoot": { "newRoot": "$doc" } },
                         { "$out": "collection" }])

result = list(coll.aggregate(
    [
        {"$group": { "_id": { "_id": "$_id","SYMBOL": "$SYMBOL", "SERIES": "$ SERIES" } } }
    ]
))

x=[]
records = db.coll.find({})
for idx in records:
    x.append({'_id.SYMBOL': idx['_id.SYMBOL'], '_id. SERIES': idx['_id. SERIES']})


print(list(x))

