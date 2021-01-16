"""
sqlite3 import which is needed for connecting to db
"""
import sqlite3

cxn = sqlite3.connect('../data/bot.db')
cxn.execute("PRAGMA foreign_keys = ON;")


def build_database():
	"""
	builds the database with the script.sql file.
	"""
	with open("script.sql", "r", encoding = "utf-8") as f:
		cxn.executescript(f.read())
	
	cxn.commit()


if __name__ == '__main__':
	build_database()
