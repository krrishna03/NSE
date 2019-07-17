import pandas as pd
import io
import requests
from pymongo import MongoClient
from connection import connect


url = "https://www.nseindia.com/products/content/sec_bhavdata_full.csv"
s = requests.get(url).content
ds = pd.read_csv(io.StringIO(s.decode('utf-8')))

db=connect()
coll=db['TEST2']

try:
    records_ = ds.to_dict(orient='records')
    result = db.TEST2.insert_many(records_)
    print("data imported")

except:
    print("could not import data")




