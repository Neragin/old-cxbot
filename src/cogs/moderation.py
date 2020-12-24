from discord import Member, Invite
from discord.ext.commands import Cog, command, has_permissions


class Moderation(Cog):
	def __init__(self, client):
		self.client = client

	@command(name = "clear", aliases = ["purge", "bulkremove", "bulkdelete", "wipe"])
	@has_permissions(manage_messages = True)
	async def clear(self, ctx, amount):
		amount: int = int(amount)
		amount += 1
		await ctx.channel.purge(limit = amount)

	@command(name = "kick", aliases = ["boot"])
	@has_permissions(kick_members = True)
	async def kick(self, ctx, member: Member, *, reason: str = None):
		await member.kick(reason = reason)
		await ctx.send(f"Kicked {member}")

	@command(name = "ban", aliases = ["exile"])
	@has_permissions(ban_members = True)
	async def ban(self, ctx, member: Member, *, reason: str = None):
		await member.ban(reason = reason)
		await ctx.send(f"banned {member}")

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

	@command(name = "delinvite")
	@has_permissions(manage_channels = True)
	async def delinvite(self, ctx, invite: Invite, reason = None):
		print(invite)
		invite = await self.client.fetch_invite(invite)
		print(invite)
		await invite.delete(reason = reason)


def setup(client):
	client.add_cog(Moderation(client))
