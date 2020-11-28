from discord.ext import commands
from discord.ext.commands import command


class ping(commands.Cog):

	def __init__(self, client):
		self.client = client

	@command()
	async def ping(self, ctx):
		await ctx.send(f'my ping is {round(self.client.latency * 1000)} ms')


def setup(client):
	client.add_cog(ping(client))
