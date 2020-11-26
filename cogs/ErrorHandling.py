from datetime import datetime

from discord import Embed, Colour
from discord.ext import commands
from discord.ext.commands import Cog, command, MissingRequiredArgument
from termcolor import colored


class Example(Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Pass in the right arguments!")


def setup(client):
	client.add_cog(Example(client))
