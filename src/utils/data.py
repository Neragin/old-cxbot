"""
CxBot uses an sqlite3 database that is stored in data/bot.db
for smaller pieces of data, cxbot stores things like # of times a command is run in json files
"""
import json
from sqlite3 import connect

DB_PATH: str = "data/bot.db"
JSON_PATH: str = "data/commands.json"

cxn = connect(DB_PATH, check_same_thread = False)
cur = cxn.cursor()


def close():
	"""
	closes connection to database
	"""
	cxn.close()


def commit():
	"""
	commits to database
	"""
	cxn.commit()


def fetchone(command, *values):
	"""
	fetches data from database
	:param command: sql command to run
	:param values: values in the sql command
	:return: data from sql db
	"""
	cur.execute(command, tuple(values))
	return cur.fetchone()


def execute(command, *values):
	"""
	execute a command in sql database
	:param command: command
	:param values: values
	"""
	cur.execute(command, values)


def fetchall(*args):
	"""
	run a fetchall on the
	:param args:
	:return:
	"""
	cur.execute(*args)
	return cur.fetchall()


def loadjson():
	"""
	load the json files
	:return: loaded file as dict
	"""
	with open(JSON_PATH) as f:
		data: dict = json.load(f)
		return data


def dumpjson(jsoncontent: dict):
	"""
	dumps the dictionary into a json file
	:param jsoncontent:
	"""
	with open(JSON_PATH, "w") as f:
		json.dump(jsoncontent, f)


def scriptexec(path):
	"""
	execute an sql script file.
	:param path:
	"""
	with open(path, "r", encoding = "utf-8") as script:
		cur.executescript(script.read())
