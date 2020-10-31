from datetime import datetime
from discord import Embed
from discord.ext.commands import Cog
class Example(Cog):
    def __init__(self, client):
        self.client = client
    @Cog.listener()
    async def on_ready(self):
        self.log_channel = self.client.get_channel(726208690763333642)
        print('monitoring cogs are online')
    @Cog.listener()
    async def on_member_update(self, before, after):
        if before.display_name != after.display_name:
            embed = Embed(title="Member update",
                          description="Nickname change",
                          colour=after.colour,
                          timestamp=datetime.utcnow())
            embed.add_field(name='Before', value=f"{before.display_name}")
            embed.add_field(name="after", value=f"{after.display_name}")
            await self.log_channel.send(embed=embed)
    @Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            if before.content != after.content:
                pass
    @Cog.listener()
    async def on_message_delete(self, before, after):
        if not after.author.bot:
            pass
def setup(client):
    client.add_cog(Example(client))