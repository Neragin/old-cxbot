from discord.ext import commands
from discord.ext.commands import command
from utils.data import loadjson, dumpjson


class Hi(commands.Cog):

	def __init__(self, client):
		self.client = client
		print(len(self.client.guilds))

	@command(name = 'Hi', aliases = ["Hello", "Yo", "Hey"])
	async def hi(self, ctx):
		await ctx.send('Hi')
		data = loadjson()
		data["hi"] += 1
		dumpjson(data)


def setup(client):
	client.add_cog(Hi(client))
