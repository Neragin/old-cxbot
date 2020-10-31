from discord.ext import commands
from discord.ext.commands import Cog
class Example(Cog):

    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        print('cog is online')
    @commands.command()
    async def hi(self, ctx):
        await ctx.send
def setup(client):
    client.add_cog(Example(client))