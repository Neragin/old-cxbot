from datetime import datetime as dt

from discord import Embed, Color
from discord.ext.commands import Cog
from utils import database as db


class GuildLogging(Cog):

	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_member_update(self, before, after):
		pass

	@Cog.listener()
	async def on_message_delete(self, message):
		global databseresult
		global loggingchannel

		try:
			databseresult = db.fetchone(f"SELECT * FROM guild WHERE GuildID = {message.guild.id}")
			loggingchannel = databseresult[1]
		except:
			print("error!")
			return

		logchannel = message.guild.get_channel(loggingchannel)

		embed = Embed(
			color = message.author.color,
			title = f"{message.content}",
			timestamp = message.created_at,
		)
		fields = [
			("author's id: ", message.author.id, True),
			("Channel's id", message.channel.id, True)


		]
		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)
		embed.set_author(name = message.author, icon_url = message.author.avatar_url)
		await logchannel.send(embed = embed)

	@Cog.listener()
	async def on_message_edit(self, before, after):
		pass

	@Cog.listener()
	async def on_member_join(self, member):
		pass

	@Cog.listener()
	async def on_member_leave(self, member):
		pass

	@Cog.listener()
	async def on_invite_create(self, invite):
		pass

	@Cog.listener()
	async def on_member_unban(self, guild, user):
		pass

	@Cog.listener()
	async def on_member_ban(self, guild, user):
		pass

	@Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		pass

	@Cog.listener()
	async def on_guild_role_update(self, guild, before, after):
		pass


def setup(client):
	client.add_cog(GuildLogging(client))
