from discord import Game, Status
from discord.ext.commands import Cog
from termcolor import colored


class Core(Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		await self.client.change_presence(status = Status.idle, activity = Game("cx help for commands"))
		print(colored('hi cogs are online', 'green'))


def setup(client):
	client.add_cog(Core(client))
