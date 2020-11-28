import os

from discord import Intents
from discord.ext.commands import Bot

from utils import ApiLogging
from utils.vars import EnvVars, Styling


class cxbot:

	def __init__(self):
		self.Intents = Intents.all()
		self.client = Bot(command_prefix = f"{EnvVars.botname} ", case_insensitive = True)

	def loadCogs(self):
		for filename in os.listdir("cogs"):
			if filename.endswith(".py"):
				self.client.load_extension(f"cogs.{filename[:-3]}")
				print(f"Loaded cog {filename[:-2]}")
		print(Styling.OKGREEN + "Finished loading all cogs!")

	def runbot(self):
		self.loadCogs()
		ApiLogging.apilogging()
		self.client.run(EnvVars.discordkey, reconnect = True)


cxbot = cxbot()
