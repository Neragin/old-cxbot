"""
imports
"""
import discord
from discord import Member, Invite, Role
from discord.ext.commands import Cog, command, has_permissions, BadArgument, MissingRequiredArgument


class Moderation(Cog):
	"""
	Moderation cog with moderation commands!
	"""
	
	def __init__(self, client):
		self.client = client
	
	@command(name = "clear", aliases = ["purge"])
	@has_permissions(manage_messages = True)
	async def clear(self, ctx, amount):
		"""
		clears the passed in amount of messages
		:param amount:
		"""
		amount: int = int(amount)
		amount += 1
		await ctx.channel.purge(limit = amount)
	
	@command(name = "kick", aliases = ["boot"])
	@has_permissions(kick_members = True)
	async def kick(self, ctx, member: Member, *, reason: str = None):
		"""
		kicks the member
		:param member:
		:param reason:
		"""
		await member.kick(reason = reason)
		await ctx.send(f"Kicked {member}")
	
	@command(name = "ban", aliases = ["exile"])
	@has_permissions(ban_members = True)
	async def ban(self, ctx, member: Member, *, reason: str = None):
		"""

		:param member:
		:param reason:
		"""
		await member.ban(reason = reason)
		await ctx.send(f"banned {member}")
	
	@command(name = "unban")
	@has_permissions(ban_members = True)
	async def unban(self, ctx, *, member: str):
		"""
		unbans member
		:param member: the member that needs to be unbanned.
		:return: confirmation that member was unbanned.
		"""
		banned_users: list = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')
		for ban_entry in banned_users:
			user = ban_entry.user
			
			if (user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'unbanned {user.mention}')
				return
	
	@command(name = "delinvite")
	@has_permissions(manage_channels = True)
	async def delete_invite(self, ctx: discord.ext.commands.Context, invite: Invite, reason = None):
		"""
		deletes the passed in invite.
		:param invite: the invite code
		:param reason: optional reason as to why the invite was deleted.
		"""
		print(invite)
		invite = await self.client.fetch_invite(invite)
		print(invite)
		await invite.delete(reason = reason)
		await ctx.send(f"deleted {invite}")
	
	@command(name = "add_role")
	@has_permissions(manage_roles = True)
	async def add_role(self, ctx: discord.ext.commands.Context, role: Role, member: Member):
		"""
		adds the argument role to the argument member.
		:param role:
		:param member:
		"""
		if role.position > member.top_role.position:
			await ctx.send(f"Warning: the '{role}' has a higher position than {member}'s highest position.", delete_after = 3)
		await member.add_roles(role)
		await ctx.send(f"Added role {role} to {member}", delete_after = 3)
	
	@add_role.error
	async def add_role_error(self, ctx: discord.ext.commands.Context, exc):
		"""
		responds to errors about add_role.
		:param exc:
		"""
		if isinstance(exc, BadArgument):
			await ctx.send("The member or role doesn't exist")
		elif isinstance(exc, MissingRequiredArgument):
			await ctx.send("please pass in the required arguments")


def setup(client: discord.client):
	"""
	required
	:param client:
	"""
	client.add_cog(Moderation(client))
