from datetime import datetime

from discord import Embed, Colour
from discord.ext import commands
from discord.ext.commands import Cog, command
from termcolor import colored

from utils import hypixelapi


class Hypixel(commands.Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		print(colored('hypixel cogs are online!', 'green'))

	@command()
	async def bedwars(self, ctx, name):
		await ctx.send('pass')
		hypixel_info = hypixelapi.averagefkdr(name)
		user = ctx.author
		embed = Embed(
			colour = Colour.blue(),
			title = f"{name}'s stats",
			description = "order goes solo, doubles, 3's, and 4's",
			timestamp = datetime.utcnow(),
		)
		embed.set_thumbnail(url = "https://vignette.wikia.nocookie.net/youtube/images/9/90/Hypixel.jpg/revision/latest?cb=20180708014516")
		# embed.set_author(name = f"Hypixel Bedwars", icon_url = f"{user.avatar_url}")
		fields = [
			("Star Count", hypixel_info[1], True),
			("Average fkdr", hypixel_info[0], True),
			("Average kdr", hypixel_info[2], True),
			("Average Winrate", hypixel_info[3], True),
			("coins", hypixel_info[4], False),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)


def setup(client):
	client.add_cog(Hypixel(client))
