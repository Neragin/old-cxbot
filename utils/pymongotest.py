import os

from pymongo import MongoClient

dbpassword = os.environ.get("DBPASS")
dbuser = os.environ.get("DBUSER")
mongoserver = os.environ.get("MONGOSERVER")
print(dbuser)
print(mongoserver)
print(dbpassword)
cluster = MongoClient(f"{mongoserver}personal?retryWrites=true&w=majority")
db = cluster["personal"]
collection = db["scheduledReminders"]

post = {"_id": 1, "name": "tim", "score": 54}
collection.insert_one(post)
