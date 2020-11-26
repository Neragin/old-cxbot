import os

from pymongo import MongoClient

dbpassword = os.environ.get("DBPASS")
dbuser = os.environ.get("DBUSER")
mongoserver = os.environ.get("MONGOSERVER")
print(dbuser)
print(mongoserver)
print(dbpassword)
cluster = MongoClient(f"{mongoserver}Bot?retryWrites=true&w=majority")
db = cluster["Bot"]
collection = db["guildData"]

post = {"_id": 1, "name": "tim", "score": 54}
collection.insert_one(post)
