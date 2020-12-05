from datetime import datetime

import requests
from discord import Embed, Colour
from discord.ext import commands
from discord.ext.commands import command

from utils import hypixelapi
from utils.hypixelapi import EnvVars


class Hypixel(commands.Cog):
	def __init__(self, client):
		self.client = client

	@command()
	async def bedwars(self, ctx, name):
		data = requests.get(f"https://api.hypixel.net/player?key={EnvVars.hypixelKey}&name={name}").json()
		embed = Embed(
			colour = Colour.blue(),
			title = f"{name}'s stats",
			description = "order goes solo, doubles, 3's, and 4's",
			timestamp = datetime.utcnow(),
		)
		embed.set_thumbnail(url = "https://vignette.wikia.nocookie.net/youtube/images/9/90/Hypixel.jpg/revision/latest?cb=20180708014516")
		fields = [
			("WinRate", hypixelapi.getBedwarsWinRate(data, "all"), True),
			("AvgFKDR", hypixelapi.getBedwarsFinalKillDeath(data, "all"), True),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)


def setup(client):
	client.add_cog(Hypixel(client))
