"""

"""
from discord import Game, Status
from discord.ext.commands import Cog, command, is_owner

from utils import data as db
from utils.vars import EnvVars, Styling


class Core(Cog):
	"""

	"""
	
	def __init__(self, client):
		self.client = client
	
	@Cog.listener()
	async def on_ready(self):
		"""

		"""
		await self.client.change_presence(status = Status.idle, activity = Game(f"{EnvVars.botname} help for commands"))
		print(f"{Styling.OKGREEN}{EnvVars.botname} is online!")
		print(len(self.client.guilds))
		print("----------adding unadded guilds into database----------")
		for guild in self.client.guilds:
			db.execute("INSERT OR IGNORE INTO guild (GuildID, LogChannel) VALUES (?, ?)", guild.id, 0)
			db.commit()
			print(f"added {guild}")
		print("Done!")
	
	@Cog.listener()
	async def on_guild_join(self, guild):
		"""

		:param guild:
		"""
		db.execute("INSERT INTO guild (GuildID, LogChannel)VALUES (?, ?)", guild.id, 0)
		db.commit()
	
	@Cog.listener()
	async def on_guild_remove(self, guild):
		"""

		:param guild:
		"""
		db.execute(f"DELETE from guild WHERE GuildID = {guild.id}")
		db.commit()
	
	@command(hidden = True)
	@is_owner()
	async def load(self, ctx, extension):
		"""

		:param extension:
		"""
		self.client.load_extension(f'cogs.{extension}')
		await ctx.send('loaded')
	
	@command(hidden = True)
	@is_owner()
	async def unload(self, ctx, extension):
		"""

		:param extension:
		"""
		if ctx.author.id == 308404126830559233:
			self.client.unload_extension(f'cogs.{extension}')
			await ctx.send(f'unloaded {extension}')
	
	@command(hidden = True)
	@is_owner()
	async def reload(self, ctx, extension):
		"""

		:param extension:
		"""
		self.client.unload_extension(f'cogs.{extension}')
		self.client.load_extension(f'cogs.{extension}')
		await ctx.send(f"reloaded {extension}")
	
	@Cog.listener()
	async def on_connect(self):
		"""

		"""
		print(f"Connected to Discord (latency: {round(self.client.latency * 1000)} ms)")
	
	@Cog.listener()
	async def on_disconnect(self):
		"""

		"""
		db.close()
		print(Styling.FAIL + "Bot disconnected")
	
	@Cog.listener()
	async def on_resumed(self):
		"""

		"""
		print("Bot resumed")
	
	@command(name = "shutdown", aliases = ["die", "kill", "terminate", "disconnect", "exit", "goboom"])
	@is_owner()
	async def shutdown(self, ctx):
		"""

		"""
		await ctx.send("I am shutting down now.")
		await self.client.change_presence(status = Status.do_not_disturb, activity = Game("Shutting down!"))
		db.close()
		await self.client.close()


def setup(client):
	"""

	:param client:
	"""
	client.add_cog(Core(client))
