from datetime import datetime
from typing import Optional

from discord import Embed, Member
from discord.ext.commands import Cog, command
from termcolor import colored


class Info(Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		print(colored('info cogs are online', 'green'))

	@command(name = "userinfo", aliases = ["ui", "memberinfo", "mi"])
	async def user_info(self, ctx, target: Optional[Member]):
		target = target or ctx.author
		embed = Embed(
			title = "User Info",
			colour = target.top_role.colour,
			timestamp = datetime.utcnow()
		)
		embed.set_thumbnail(url = target.avatar_url)

		fields = [
			("ID", target.id, False),
			("Name", target.mention, True),
			("Tag", target, True),
			("Bot?", target.bot, True),
			("Top role", target.top_role.mention, True),
			("Created at", target.created_at.strftime("%m/%d/%Y %H:%M:%S"), True),
			("Joined at", target.joined_at.strftime("%m/%d/%Y %H:%M:%S"), True),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)

	@command(name = "serverinfo", aliases = ["si", "guildinfo", "gi"])
	async def server_info(self, ctx):
		embed = Embed(
			title = "Server Info",
			timestamp = datetime.utcnow()
		)
		embed.set_thumbnail(url = ctx.guild.icon_url)

		fields = [
			("ID", ctx.guild.id, False),
			("Region", ctx.guild.region, True),
			("Owner", ctx.guild.owner, True),
			("Name", ctx.guild.name, True),
			("Roles", len(ctx.guild.roles), True),
			("created at", ctx.guild.created_at, True),
			("Member count", ctx.guild.member_count, True),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)


def setup(client):
	client.add_cog(Info(client))
