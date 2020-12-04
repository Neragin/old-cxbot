from discord import Game, Status
from discord.ext.commands import Cog, command, is_owner

from utils import Database
from utils.vars import EnvVars, Styling


class Core(Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		await self.client.change_presence(status = Status.idle, activity = Game(f"{EnvVars.botname} help for commands"))
		print(f"{Styling.OKGREEN}{EnvVars.botname} is online!")
		print(self.client.guilds)

	@Cog.listener()
	async def on_guild_join(self, guild):
		print(f"I have joined {guild}")
		Database.execute("INSERT INTO guild (GuildID, LogChannel)VALUES (?, ?)", guild.id, 0)
		Database.commit()

	@Cog.listener()
	async def on_guild_remove(self, guild):
		Database.execute(f"DELETE from guild WHERE GuildID = {guild.id}")
		Database.commit()

	@command(hidden = True)
	@is_owner()
	async def load(self, ctx, extension):
		self.client.load_extension(f'cogs.{extension}')
		await ctx.send('loaded')

	@command(hidden = True)
	@is_owner()
	async def unload(self, ctx, extension):
		if ctx.author.id == 308404126830559233:
			self.client.unload_extension(f'cogs.{extension}')
			await ctx.send(f'unloaded {extension}')

	@command(hidden = True)
	@is_owner()
	async def reload(self, ctx, extension):
		self.client.unload_extension(f'cogs.{extension}')
		self.client.load_extension(f'cogs.{extension}')
		await ctx.send(f"reloaded {extension}")

	@Cog.listener()
	async def on_connect(self):
		print(f"Connected to Discord (latency: {round(self.client.latency * 1000)} ms)")

	@Cog.listener()
	async def on_disconnect(self):
		print(Styling.FAIL + "Bot disconnected")

	@Cog.listener()
	async def on_resumed(self):
		print("Bot resumed")


def setup(client):
	client.add_cog(Core(client))
