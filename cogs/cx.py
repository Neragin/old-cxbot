from discord.ext.commands import command, Cog
from termcolor import colored


class cx(Cog):

	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		print(colored('cx cogs are online', 'green'))

	@command(name = "speak", hidden = True)
	async def speak(self, ctx, text, *, message):
		if ctx.author.id == 308404126830559233:
			channel = self.client.get_channel(int(text))
			await channel.send(message)


def setup(client):
	client.add_cog(cx(client))
