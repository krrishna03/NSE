import json
import pandas as pd
from pymongo import MongoClient

client=MongoClient('localhost:27017')
db=client['NSE1']
coll=db['TEST1']

df=pd.read_csv("day_1.csv")
json_data=json.loads(df.to_json(orient='records'))
db.TEST2.insert(json_data)

df=pd.read_csv("day_2.csv")
json_data=json.loads(df.to_json(orient='records'))
db.TEST3.insert(json_data)

df=pd.read_csv("day_3.csv")
json_data=json.loads(df.to_json(orient='records'))
db.TEST4.insert(json_data)