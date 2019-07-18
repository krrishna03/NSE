from pymongo import MongoClient


def connect():
    try:
        client = MongoClient('localhost', 27017)
        print("connected to database")
        db = client['NSE1']

        return db
    
    except:
        print("Could not connect")


