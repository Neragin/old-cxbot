from discord.ext import commands
from discord.ext.commands import command

from utils import catapi


class EmotionalSupport(commands.Cog):

	def __init__(self, client):
		self.client = client

	@command(name = 'EmotionalSupport', aliases = ["emo", 'emotional', "emosupport"])
	async def emotionalsupport(self, ctx):
		await ctx.send(catapi.getCat())


def setup(client):
	client.add_cog(EmotionalSupport(client))
