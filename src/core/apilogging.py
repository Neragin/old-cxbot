"""
logss
"""
import logging


def apilogging():
	"""
	logs data from the API into logs/discordapi.log so that I can fix cxbot incase cxbot goes boom
	"""
	logger = logging.getLogger('discord')
	logger.setLevel(logging.DEBUG)
	handler = logging.FileHandler(filename = 'logs/discordapi.log', encoding = 'utf-8', mode = 'w')
	handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
	logger.addHandler(handler)
	print("Started logging ApiData")
