"""
necessary imports from discord.
"""
import discord
from discord.ext import commands
from discord.ext.commands import command, Cog

from utils.data import loadjson, dumpjson


class Hi(Cog):
	"""
	The Hi class. extends Cogs for cog functionality
	"""
	
	def __init__(self, client):
		self.client: discord.client = client
		print(len(self.client.guilds))
	
	@command(name = 'Hi', aliases = ["Hello", "Yo", "Hey"])
	async def hi(self, ctx: discord.ext.commands.Context):
		"""
		says hi :D
		:param ctx: context for action, required.
		"""
		await ctx.send('Hi')
		data: dict = loadjson()
		data["hi"] += 1
		dumpjson(data)


def setup(client: discord.client):
	"""
	required for cogs
	:param client: cxbot
	"""
	client.add_cog(Hi(client))
