import platform
from datetime import datetime

import discord
import psutil
from discord import Embed
from discord.ext.commands import Cog, command

from utils.Vars import EnvVars


class Botinfo(Cog):
	def __init__(self, client):
		self.client = client

	@command(name = "invitelink", description = "Sends invite link")
	async def invite(self, ctx):
		await ctx.send("https://discord.com/api/oauth2/authorize?client_id=718284261358174250&permissions=8&scope=bot is the invite link to the bot!")

	@command(name = "botinfo")
	async def system_info(self, ctx):
		embed = Embed(
			color = ctx.author.color,
			title = f"Info of {EnvVars.botname} Bot",
			timestamp = datetime.utcnow(),
		)
		fields = [
			("CPU percentage =", psutil.cpu_percent(), True),
			("RAM percentage =", psutil.virtual_memory().percent, True),
			("Discord.py version = ", discord.__version__, True),
			("Python Version = ", platform.python_version(), True),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)


def setup(client):
	client.add_cog(Botinfo(client))
