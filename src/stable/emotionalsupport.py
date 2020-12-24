from discord.ext import commands
from discord.ext.commands import command

from utils.catapi import getcat
from utils.data import loadjson, dumpjson


class EmotionalSupport(commands.Cog):

	def __init__(self, client):
		self.client = client

	@command(name = 'EmotionalSupport', aliases = ['emotional', "emosupport"])
	async def emotionalsupport(self, ctx):
		await ctx.send(getcat())
		data = loadjson()
		data["emotionalsupport"] += 1
		dumpjson(data)


def setup(client):
	client.add_cog(EmotionalSupport(client))
