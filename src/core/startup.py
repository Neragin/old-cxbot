import os

from discord import Intents
from discord.ext.commands import Bot, when_mentioned_or
from core import apilogging
from utils.vars import EnvVars, Styling

PREFIX = f"{EnvVars.botname} "


def get_prefix(bot, message):
	return when_mentioned_or(PREFIX)(bot, message)


class CxBot:

	def __init__(self):
		intents = Intents.all()
		self.client = Bot(command_prefix = get_prefix, case_insensitive = True, intents = intents)

	def loadcogs(self):
		for filename in os.listdir("cogs"):
			if filename.endswith(".py"):
				self.client.load_extension(f"cogs.{filename[:-3]}")
				print(f"Loaded cog {filename[:-2]}")
		print(Styling.OKGREEN + "Finished loading all cogs!")
		
	def loadcommands(self):
		for filename in os.listdir("stable"):
			if filename.endswith(".py"):
				self.client.load_extension(f"stable.{filename[:-3]}")
				print(f"Loaded cog {filename[:-2]}")
		print(Styling.OKGREEN + "Finished loading all stable commands!")

	def runbot(self):
		self.loadcogs()
		self.loadcommands()
		apilogging.apilogging()
		self.client.run(EnvVars.discordkey, reconnect = True)


CxBot = CxBot()
