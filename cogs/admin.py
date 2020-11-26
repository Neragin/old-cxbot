from discord import Member
from discord.ext.commands import Cog, command, has_permissions
from termcolor import colored


class Admin(Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		print(colored('Admin cogs are online', 'green'))

	@command(name = "clear", aliases = ["purge", "bulkremove", "bulkdelete", "wipe"])  # boilerplate code for cogs
	@has_permissions(manage_messages = True)
	async def clear(self, ctx, amount):
		amount = int(amount)
		amount += 1
		await ctx.channel.purge(limit = amount)

	@command(name = "kick", aliases = ["boot"])
	@has_permissions(kick_members = True)
	async def kick(self, ctx, member: Member, *, reason = None):
		await member.kick(reason = reason)

	@command(name = "ban", aliases = ["exile"])
	@has_permissions(ban_members = True)
	async def ban(self, ctx, member: Member, *, reason = None):
		await member.ban(reason = reason)

	@command(name = "unban")
	@has_permissions(ban_members = True)
	async def unban(self, ctx, *, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')
		for ban_entry in banned_users:
			user = ban_entry.user

			if (user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'unbanned {user.mention}')
				return


def setup(client):
	client.add_cog(Admin(client))
