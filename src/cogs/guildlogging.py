"""
imports
"""
import discord
from discord import Embed
from discord.ext.commands import Cog

from utils import data as db


class GuildLogging(Cog):
	"""
	Class for guildlogging backend code
	"""
	
	def __init__(self, client: discord.client):
		self.client = client
	
	# @Cog.listener()
	# async def on_member_update(self, before, after):
	# 	print("yes")
	# 	databseresult: list = db.fetchone(f"SELECT * FROM guild WHERE GuildID = {before.guild.id}")
	# 	loggingchannel = databseresult[1]
	# 	if loggingchannel == 0 or loggingchannel is None:
	# 		return
	# 	logchannel = before.guild.get_channel(loggingchannel)
	# 	if before.avatar_url != after.avatar_url:
	# 		embed = Embed(
	# 			color = after.color,
	# 			title = f"{after} has changed their avatar!!",
	# 			timestamp = after.joined_at,
	# 		)
	# 		fields = [
	# 			("Member ID: ", f"{before.id}", True),
	# 		]
	#
	# 		for name, value, inline in fields:
	# 			embed.add_field(name = name, value = value, inline = inline)
	# 		embed.set_author(name = after.mention, icon_url = after.avatar_url)
	# 		await logchannel.send(embed = embed)
	
	@Cog.listener()
	async def on_message_delete(self, message: discord.message):
		"""
		a listener for deleted messages
		:param message: the message sent to the
		:return: message to logging channels that were in the database
		"""
		databseresult = db.fetchone(f"SELECT * FROM guild WHERE GuildID = {message.guild.id}")
		loggingchannel = databseresult[1]
		if loggingchannel == 0 or loggingchannel is None:
			return
		logchannel = message.guild.get_channel(loggingchannel)
		embed = Embed(
			color = message.author.color,
			title = "A message was deleted!",
			timestamp = message.created_at,
		)
		fields = [
			("content: ", f"{message.content}", False),
			("Channel's id", f"{message.channel.id}", True)
		
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		embed.set_author(name = message.author, icon_url = message.author.avatar_url)
		embed.set_footer(text = f"Member id: {message.author.id}")
		await logchannel.send(embed = embed)
	
	@Cog.listener()
	async def on_message_edit(self, before: discord.message, after: discord.message):
		"""
		called when a message is edited
		:param before: the message before
		:param after: the message after
		:return: an embed if the message was sent in a channel with logging enabled
		"""
		databseresult: dict = db.fetchone(f"SELECT * FROM guild WHERE GuildID = {before.guild.id}")
		loggingchannel = databseresult[1]
		if loggingchannel == 0 or loggingchannel is None:
			return
		logchannel = before.guild.get_channel(loggingchannel)
		if before.content != after.content:
			embed = Embed(
				color = before.author.color,
				title = "A message was edited!",
				timestamp = after.created_at,
			)
			fields = [
				("Before: ", before.content or '\u200B', False),
				("After: ", after.content or '\u200B', False),
				("Channel's id", before.channel.id or '\u200B', True),
			]
			for name, value, inline in fields:
				embed.add_field(name = name, value = value, inline = inline)
			embed.set_author(name = before.author, icon_url = before.author.avatar_url)
			embed.set_footer(text = f"Member id: {before.author.id}")
			await logchannel.send(embed = embed)
		else:
			pass
	
	@Cog.listener()
	async def on_member_join(self, member: discord.member):
		"""
		called when a member joins
		:param member: the member that joined
		:return:
		"""
		print(member)
		print("pass")
		databseresult = db.fetchone(f"SELECT * FROM guild WHERE GuildID = {member.guild.id}")
		print("pass2")
		loggingchannel = databseresult[1]
		if loggingchannel == 0 or loggingchannel is None:
			return
		logchannel = member.guild.get_channel(loggingchannel)
		
		embed = Embed(
			# color = member.color,
			title = f"{member} has joined {member.guild.name}!",
			# timestamp = member.joined_at,
		)
		fields = [
			("Member ID: ", f"{member.id}", True),
		]
		
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		embed.set_author(name = member, icon_url = member.avatar_url)
		embed.set_footer(text = f"Member id: {member.id}")
		await logchannel.send(embed = embed)
	
	@Cog.listener()
	async def on_member_remove(self, member: discord.member):
		"""

		:param member:
		:return:
		"""
		print("pass")
		databseresult = db.fetchone(f"SELECT * FROM guild WHERE GuildID = {member.guild.id}")
		loggingchannel = databseresult[1]
		if loggingchannel == 0 or loggingchannel is None:
			return
		logchannel = member.guild.get_channel(loggingchannel)
		print("pass")
		embed = Embed(
			# color = member.color,
			title = f"{member} has left {member.guild.name}!",
			timestamp = member.joined_at,
		)
		embed.set_author(name = member, icon_url = member.avatar_url)
		embed.set_footer(text = f"member ID: {member.id}")
		await logchannel.send(embed = embed)
	
	@Cog.listener()
	async def on_invite_create(self, invite):
		"""

		:param invite:
		:return:
		"""
		databseresult = db.fetchone(f"SELECT * FROM guild WHERE GuildID = {invite.guild.id}")
		loggingchannel = databseresult[1]
		if loggingchannel == 0 or loggingchannel is None:
			return
		logchannel = invite.guild.get_channel(loggingchannel)
		
		embed = Embed(
			color = invite.inviter.color,
			title = "An invite link for this server was made!",
			timestamp = invite.created_at,
		)
		fields = [
			("invite code: ", f"{invite.code}", True),
			("invite expiry time: ", f"{invite.max_age}", True),
			("invite channel: ", f"{invite.channel}", True),
		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		embed.set_author(name = invite.inviter, icon_url = invite.inviter.avatar_url)
		embed.set_footer(text = f"author id: {invite.inviter.id}")
		await logchannel.send(embed = embed)
	
	@Cog.listener()
	async def on_member_unban(self, guild, user):
		"""

		:param guild:
		:param user:
		"""
		pass
	
	@Cog.listener()
	async def on_member_ban(self, guild, user):
		"""

		:param guild:
		:param user:
		"""
		pass
	
	@Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		"""

		:param member:
		:param before:
		:param after:
		"""
		pass
	
	@Cog.listener()
	async def on_guild_role_update(self, guild, before, after):
		"""

		:param guild:
		:param before:
		:param after:
		"""
		pass


def setup(client):
	"""

	:param client:
	"""
	client.add_cog(GuildLogging(client))
