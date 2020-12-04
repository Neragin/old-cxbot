from discord.ext import commands
from discord.ext.commands import command


class ping(commands.Cog):

	def __init__(self, client):
		self.client = client

	@command(name = 'Hi', aliases = ["Hello", "Yo", "Hey"])
	async def hi(self, ctx):
		await ctx.send('Hi')


def setup(client):
	client.add_cog(ping(client))
