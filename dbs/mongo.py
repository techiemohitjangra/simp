# used to store user feedback
import pymongo
import os

pymongo.AsyncMongoClient


def connect(dbPath: str = os.getenv("MONGO_DB_URI")):
    pass
