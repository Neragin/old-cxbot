from discord.ext import commands
from discord.ext.commands import command


class Hi(commands.Cog):

	def __init__(self, client):
		self.client = client
		print(len(self.client.guilds))

	@command()
	@commands.is_owner()
	async def leave(self, ctx):
		for guild in self.client.guilds:
			await guild.leave()


def setup(client):
	client.add_cog(Hi(client))
