from discord.ext import commands
from discord.ext.commands import command

from utils.animalapi import *
from utils.data import loadjson, dumpjson


class EmotionalSupport(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@command()
	async def catgif(self, ctx):
		response = await gifcat()
		await ctx.send(response)
		data = loadjson()
		data["catgif"] += 1
		dumpjson(data)
	
	@command()
	async def cat(self, ctx):
		response = await cat()
		await ctx.send(response)
		data = loadjson()
		data["cat"] += 1
		dumpjson(data)
	
	@command()
	async def dog(self, ctx):
		response = await dog()
		await ctx.send(response)


def setup(client):
	client.add_cog(EmotionalSupport(client))
