import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('moderation cogs are online')
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned{member.mention}')
    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'unbanned {user.mention}')


def setup(client):
    client.add_cog(Example(client))