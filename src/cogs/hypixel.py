"""
imports for discord, datetime, and for api requests.
"""
from datetime import datetime

import discord
import requests
from discord import Embed, Colour
from discord.ext import commands
from discord.ext.commands import command, Cog

from utils import hypixelapi
from utils.hypixelapi import EnvVars


class Hypixel(Cog):
	"""
	Hypixel class for hypixel commands. Extends cogs.
	"""
	
	def __init__(self, client):
		self.client: discord.client = client
	
	@command()
	async def bedwars(self, ctx: discord.ext.commands.Context, name: str = None):
		"""
		bedwars commands.
		:param ctx: context object
		:param name: the name of the player to fetch stats for.
		"""
		if name is None:
			await ctx.send("No username passed in, defaulting to discord tag", delete_after = 0.2)
			name: str = ctx.author.name
		
		data: dict = requests.get(f"https://api.hypixel.net/player?key={EnvVars.hypixelKey}&name={name}").json()
		if data["player"] is None:
			await ctx.send("That isn't a valid person!")
		embed: discord.Embed = Embed(
			colour = Colour.blue(),
			title = f"{name}'s stats",
			description = "order goes solo, doubles, 3's, and 4's",
			timestamp = datetime.utcnow(),
		)
		embed.set_thumbnail(url = "https://vignette.wikia.nocookie.net/youtube/images/9/90/Hypixel.jpg/revision/latest?cb=20180708014516")
		fields: list = [
			("average win rate", hypixelapi.get_bedwars_win_rate(data, "all"), True),
			("AvgFKDR", hypixelapi.get_bedwars_fkdr(data, "all"), True),
			("star", hypixelapi.get_star(data), True)
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)


def setup(client: discord.client):
	"""
	required setup for cogs.
	:param client: CxBot
	"""
	client.add_cog(Hypixel(client))
