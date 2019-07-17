from connection import connect

db = connect()
coll = db['TEST2']

x = []
records = db.TEST2.find({})
for idx in records:
    x.append({'SYMBOL': idx['SYMBOL'], ' SERIES': idx[' SERIES']})

print(x)
db.company_info.insert(x)
y = []
records1= db.TEST2.find({})
for idx in records1:
    y.append({' DATE1': idx[' DATE1'],
              ' PREV_CLOSE': idx[' PREV_CLOSE'],
              ' OPEN_PRICE': idx[' OPEN_PRICE'],
              ' HIGH_PRICE':idx[' HIGH_PRICE'],
              ' LOW_PRICE':idx[' LOW_PRICE'],
              ' LAST_PRICE':idx[' LAST_PRICE'],
              ' CLOSE_PRICE':idx[' CLOSE_PRICE'],
              ' AVG_PRICE':idx[' AVG_PRICE'],
              ' TTL_TRD_QNTY':idx[' TTL_TRD_QNTY'],
              ' TURNOVER_LACS':idx[' TURNOVER_LACS'],
              ' NO_OF_TRADES':idx[' NO_OF_TRADES'],
              ' DELIV_QTY':idx[' DELIV_QTY'],
              ' DELIV_PER':idx[' DELIV_PER']})

print(list(y))
db.company_data.insert(y)







"""
cursor = db.coll.find({},{"SYMBOL": "DHFL","SERIES": "EQ"})
#x=[]
Cur= db.TEST2.find({ '$and' : [{"SYMBOL": "DHFL"} , {"SERIES" : "EQ"}]})

for i in Cur:
    x.append(i)

print(x)

for idx in cursor:
    print(idx)
#Cur = db.TEST2.find({}, {"SYMBOL": 1, "SERIES": 1, "DATE1": 1})
"""
