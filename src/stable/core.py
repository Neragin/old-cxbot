from discord.ext.commands import Cog

from utils import data as db


class Core(Cog):
	def __init__(self, client):
		self.client = client
	
	@Cog.listener()
	async def on_guild_join(self, guild):
		db.execute("INSERT INTO guild (GuildID, LogChannel)VALUES (?, ?)", guild.id, 0)
		db.commit()
	
	@Cog.listener()
	async def on_guild_remove(self, guild):
		db.execute(f"DELETE from guild WHERE GuildID = {guild.id}")
		db.commit()


def setup(client):
	client.add_cog(Core(client))
