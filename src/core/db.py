import sqlite3
import datetime as dt
import random

cxn = sqlite3.connect('../data/bot.db')
cxn.execute("PRAGMA foreign_keys = ON;")


def build_database():
	with open("script.sql", "r", encoding = "utf-8") as f:
		cxn.executescript(f.read())

	cxn.commit()


if __name__ == '__main__':
	build_database()
