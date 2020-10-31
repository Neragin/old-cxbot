from utils import hypixelapi
from discord import Embed, Colour
from discord.ext import commands
from datetime import datetime
class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('hypixel cogs are online')
    @commands.command()
    async def bedwars(self, ctx, name):
        await ctx.send('pass')
        hypixel_info = hypixelapi.averagefkdr(name)
        user = ctx.author
        embed = Embed(
            colour=Colour.blue(),
            title=f"{name}'s stats",
            description="order goes solo, doubles, 3's, and 4's",
            timestamp=f"{datetime.utcnow()}"
        )
        embed.set_author(name=f"Hypixel Bedwars", icon_url=f"{user.avatar_url}")
        embed.add_field(name="Star Count", value=f"{hypixel_info[1]}")
        embed.add_field(name="average fkdr", value=f"{hypixel_info[0]}")
        embed.add_field(name="average kdr", value=f"{hypixel_info[2]}")
        embed.add_field(name="average winrate", value=f"{hypixel_info[3]}", inline=False)
        embed.add_field(name="coins", value=f"{hypixel_info[4]}", )
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(Example(client))