"""

"""
from datetime import datetime
from typing import Optional

from discord import Embed, Member
from discord.ext.commands import Cog, command


class GuildInfo(Cog):
	"""

	"""
	
	def __init__(self, client):
		self.client = client
	
	@command(name = "userinfo", aliases = ["ui", "memberinfo", "mi"])
	async def user_info(self, ctx, user: Optional[Member]):
		"""

		:param user:
		"""
		user = user or ctx.author
		embed = Embed(
			title = "User Info",
			colour = user.top_role.colour,
			timestamp = datetime.utcnow()
		)
		embed.set_thumbnail(url = user.avatar_url)
		
		fields = [
			("ID", user.id, False),
			("Name", user.mention, True),
			("Tag", user, True),
			("Bot?", user.bot, True),
			("Top role", user.top_role.mention, True),
			("Created at", user.created_at.strftime("%m/%d/%Y %H:%M:%S"), True),
			("raw status", user.raw_status or '\u200B', True),
			("Joined at", user.joined_at.strftime("%m/%d/%Y %H:%M:%S"), True),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)
	
	"""
	Shows Server Info 
	gets the server ID, Region, Owner, Name, amount of roles, when server was made, and the member count
	
	name = serverinfo
	aliases = si, guildinfo, gi
	"""
	
	@command(name = "serverinfo", aliases = ["si", "guildinfo", "gi"])
	async def server_info(self, ctx):
		"""
		Gets info about server
		"""
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
			("created at", ctx.guild.created_at.strftime("%m/%d/%Y %H:%M:%S"), True),
			("Member count", ctx.guild.member_count, True),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		await ctx.send(embed = embed)


def setup(client):
	"""

	:param client:
	"""
	client.add_cog(GuildInfo(client))
