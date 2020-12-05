from sqlite3 import connect

DB_PATH = "data/bot.db"

cxn = connect(DB_PATH, check_same_thread = False)
cur = cxn.cursor()


def close():
	cxn.close()


def commit():
	cxn.commit()


def fetchone(command, *values):
	cur.execute(command, tuple(values))
	return cur.fetchone()


def execute(command, *values):
	cur.execute(command, values)


def fetchall(*args):
	cur.execute(*args)
	return cur.fetchall()


def scriptexec(path):
	with open(path, "r", encoding = "utf-8") as script:
		cur.executescript(script.read())
