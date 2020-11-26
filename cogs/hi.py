from datetime import datetime

from discord import Embed, Colour
from discord.ext.commands import Cog, command
from termcolor import colored


class Example(Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		print(colored('hi cogs are online', 'green'))

	@command()
	async def hi(self, ctx):
		await ctx.send("HELLO PERSON")
		embed = Embed(
			colour = Colour.blue(),
			title = f"fasdff's stats",
			description = "order goes solo, doubles, 3's, and 4's",
			timestamp = datetime.utcnow(),
		)
		embed.set_thumbnail(url = "https://vignette.wikia.nocookie.net/youtube/images/9/90/Hypixel.jpg/revision/latest?cb=20180708014516")
		fields = [
			("coins", "value", False),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)

def setup(client):
	client.add_cog(Example(client))
