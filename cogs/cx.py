from discord.ext import commands
from termcolor import colored


class cx(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print(colored('cx cogs are online', 'green'))

	@commands.command(hidden = True)
	async def speak(self, ctx, text, *, message):
		if ctx.author.id == 308404126830559233:
			channel = self.client.get_channel(int(text))
			await channel.send(message)
		else:
			await ctx.send('no')


def setup(client):
	client.add_cog(cx(client))
