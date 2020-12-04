from discord.ext import commands
from discord.ext.commands import command, Cog


class Owner(Cog):

	def __init__(self, client):
		self.client = client

	@command(name = "speak", hidden = True)
	@commands.is_owner()
	async def speak(self, ctx, text, *, message):
		channel = self.client.get_channel(int(text))
		await channel.send(message)

	@speak.error
	async def speak_error(self, ctx, error):
		if isinstance(error, commands.CheckFailure):
			await ctx.send("You aren't my Owner!")
		else:
			raise error


def setup(client):
	client.add_cog(Owner(client))
