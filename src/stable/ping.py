"""

"""
from discord.ext import commands
from discord.ext.commands import command


class Ping(commands.Cog):
	"""
	Bots Ping
	"""
	
	def __init__(self, client):
		self.client = client
	
	@command()
	async def ping(self, ctx):
		"""
		Responds with the ping of CxBot
		"""
		await ctx.send(f'my Ping is {round(self.client.latency * 1000)} ms')


def setup(client):
	"""

	:param client:
	"""
	client.add_cog(Ping(client))
