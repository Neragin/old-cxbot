"""
CxBot uses an sqlite3 database that is stored in data/bot.db
for smaller pieces of data, cxbot stores things like # of times a command is run in json files
"""
import json
from os.path import isfile
from sqlite3 import connect

from apscheduler.triggers.cron import CronTrigger

DB_PATH: str = "data/bot.db"
JSON_PATH: str = "data/commands.json"
BUILD: str = "core/script.sql"

cxn = connect(DB_PATH, check_same_thread = False)
cur = cxn.cursor()


def with_commit(func):
	"""
	with commit decorator
	:param func:
	:return:
	"""
	
	def inner(*args, **kwargs):
		func(*args, **kwargs)
		commit()
	
	return inner


@with_commit
def build():
	if isfile(BUILD):
		scriptexec(BUILD)


def close():
	cxn.close()


def commit():
	cxn.commit()


def fetchone(command, *values):
	cur.execute(command, tuple(values))
	return cur.fetchone()


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


# def field(command, *values):
# 	cur.execute(command, tuple(values))
#
# 	if (fetch := cur.fetchone()) is not None:
# 		return fetch[0]


def record(command, *values):
	cur.execute(command, tuple(values))
	
	return cur.fetchone()


def records(command, *values):
	cur.execute(command, tuple(values))
	
	return cur.fetchall()


def column(command, *values):
	cur.execute(command, tuple(values))
	
	return [item[0] for item in cur.fetchall()]


def execute(command, *values):
	cur.execute(command, tuple(values))


def multiexec(command, valueset):
	cur.executemany(command, valueset)


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


def autosave(scheduler):
	scheduler.add_job(commit, CronTrigger(second = 0))
