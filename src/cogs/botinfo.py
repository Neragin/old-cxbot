"""
imports to get bot's info
"""
from datetime import datetime

import discord
import psutil
from discord import Embed
from discord.ext.commands import Cog, command

from utils.data import loadjson
from utils.vars import EnvVars, TrackedCmds


class Botinfo(Cog):
	"""
	Cog with all of the bot info
	"""
	
	def __init__(self, client):
		self.client: discord.ext.commands.Bot = client
	
	@command(name = "invitelink", description = "Sends invite link")
	async def invite(self, ctx: discord.ext.commands.Context):
		"""
		Sends invite link
		:param ctx: Context Object
		"""
		await ctx.send("https://discord.com/api/oauth2/authorize?client_id=718284261358174250&permissions=8&scope=bot is the invite link to the bot!")
	
	@command(name = "botinfo")
	async def system_info(self, ctx: discord.ext.commands.Context):
		"""
		shows system info like cpu, and ram
		"""
		embed: discord.Embed = Embed(
			color = ctx.author.color,
			title = f"Info of {EnvVars.botname} Bot",
			timestamp = datetime.utcnow(),
		)
		fields: list = [
			("CPU percentage =", psutil.cpu_percent(), True),
			("RAM percentage =", psutil.virtual_memory().percent, True),
			("Discord.py version = ", discord.__version__, True),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)
	
	@command()
	async def cmdstats(self, ctx: discord.ext.commands.Context, commands: str):
		"""
		shows how many times a command was run
		:param commands: the command to check for
		"""
		if commands.lower() in TrackedCmds.commands:
			data: dict = loadjson()
			await ctx.send(f"commands was sent {data[commands]} times!")
		else:
			await ctx.send(f"That command isn't tracked! {EnvVars.botname} only tracks the usage of 2 commands, which are `hi`, and `emotionalsupport`")


def setup(client: discord.ext.commands.Bot):
	"""
	sets up the cog
	:param client: cxbot
	"""
	client.add_cog(Botinfo(client))
