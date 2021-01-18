import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Intents, Status, Game
from discord.ext.commands import Bot as BaseBot, CommandNotFound

from core.apilogging import apilogging
from utils import data as db
from utils.vars import EnvVars, Styling

OWNER_ID = [308404126830559233]


class Bot(BaseBot):
	def __init__(self):
		self.PREFIX = f"{EnvVars.botname} "
		self.scheduler = AsyncIOScheduler
		self.ready = False
		super().__init__(command_prefix = 'cx ', case_insensitive = True, owner_ids = OWNER_ID, intents = Intents.all())
	
	def run(self):
		self.loadcogs()
		self.loadcommands()
		apilogging()
		print("running bot")
		super().run(EnvVars.discordkey, reconnect = True)
	
	def loadcogs(self):
		for filename in os.listdir("cogs"):
			if filename.endswith(".py"):
				super().load_extension(f"cogs.{filename[:-3]}")
				print(f"loaded cog {filename[:-2]}")
		print(Styling.OKGREEN + "finished loading all cogs!")
	
	def loadcommands(self):
		for filename in os.listdir("stable"):
			if filename.endswith(".py"):
				print(f"loaded command {filename[:-2]}")
		print(Styling.OKGREEN + "Finished loading all commands!")
	
	async def on_connect(self):
		print("CxBot is connected")
	
	async def on_disconnect(self):
		print("CxBot is Disconnected")
	
	async def on_error(self, event_method, *args, **kwargs):
		raise
	
	async def on_command_error(self, ctx, exc):
		if isinstance(exc, CommandNotFound):
			pass
		elif hasattr(exc, "original"):
			raise exc.original
		else:
			raise exc
	
	async def on_ready(self):
		if not self.ready:
			self.ready = True
			print("CxBot is ready")
			await super().change_presence(status = Status.idle, activity = Game(f"{self.PREFIX} help for commands"))
			print("---------------------adding unadded guilds into database-----------------")
			for guild in super().guilds:
				db.execute("INSERT OR IGNORE INTO guild (GuildID, LogChannel) VALUES (?, ?)", guild.id, 0)
				db.commit()
			print("Done!")
		else:
			print("CxBot has reconnected")


bot = Bot()
