from discord.ext.commands import Cog, MissingRequiredArgument


class Example(Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Pass in the right arguments!")

		raise


def setup(client):
	client.add_cog(Example(client))
