"""
required imports.
"""
import discord
from discord.ext.commands import Cog, MissingRequiredArgument


class ErrorHandling(Cog):
	"""
	"Handles CxBot's Errors. Errors can be dealt with here, or dealt with command specifically."
	"""
	
	def __init__(self, client):
		self.client: discord.client = client
	
	@Cog.listener()
	async def on_command_error(self, ctx: discord.ext.commands.Context, error: discord.ext.commands.CommandError):
		"""
		Main method that handles errors. Can handle MissingRequiredArgument.
		:param self: self
		:param ctx: context
		:param error: the error that occurred.
		"""
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Pass in the right arguments!")
		raise


def setup(client: discord.client):
	"""
	required for the cog to be loaded.
	:param client: cxbot's client
	"""
	client.add_cog(ErrorHandling(client))
