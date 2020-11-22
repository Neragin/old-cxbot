from discord.ext import commands
from discord.ext.commands import Cog, command
from termcolor import colored


class Example(Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		print(colored('hi cogs are online', 'green'))

	@command()  # boilerplate code for cogs
	async def hi(self, ctx):
		await ctx.send("HELLO PERSON")


def setup(client):
	client.add_cog(Example(client))
