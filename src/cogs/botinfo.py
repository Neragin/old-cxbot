from datetime import datetime

import psutil
from discord import Embed
from discord.ext.commands import Cog, command
from termcolor import colored


class Botinfo(Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		print(colored('hi cogs are online', 'green'))

	@command(name = "invitelink", description = "Sends invite link")
	async def invite(self, ctx):
		await ctx.send("https://discord.com/api/oauth2/authorize?client_id=718284261358174250&permissions=8&scope=bot is the invite link to the bot!")

	@command(name = "sysinfo")
	async def system_info(self, ctx):
		embed = Embed(
			color = ctx.author.color,
			title = "System info of Cx Bot",
			description = "The AWS server's system information",
			timestamp = datetime.utcnow(),
		)
		fields = [
			("CPU percentage =", psutil.cpu_percent(), True),
			("RAM percentage =", psutil.virtual_memory().percent, True),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)


def setup(client):
	client.add_cog(Botinfo(client))
