from pymongo import MongoClient


def connect():
    try:
        client = MongoClient('localhost', 27017)
        print("connected to database")

    except:
        print("Could not connect")

    db = client['NSE1']

    return db
