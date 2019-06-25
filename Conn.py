import json
from pymongo import MongoClient
import io
from pymongo import ReadPreference
import bson
import pandas as pd
from bson import *


client=MongoClient('localhost:27017')
db=client['NSE1']
coll=db['TEST1']

