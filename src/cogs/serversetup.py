from discord import TextChannel
from discord.ext import commands
from discord.ext.commands import has_permissions

from utils import data as db
from utils.vars import EnvVars


class ServerSetup(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.group(invoke_without_command = True)
	async def setup(self, ctx):
		await ctx.send(f"Hello! I am the wizard for {EnvVars.botname} bot. This command is for a group of commands, so use {EnvVars.botname} setup <command>")

	@setup.command()
	@has_permissions(manage_messages = True)
	async def logging(self, ctx, channel: TextChannel):
		await ctx.send(channel)
		if type(channel) == TextChannel and channel.guild == ctx.guild:
			await ctx.send("found channel")
		else:
			await ctx.send("That either isn't a valid channel(hint: use #channelname), or that channel isn't in this server")
		db.execute(f"UPDATE guild SET LogChannel = {channel.id} WHERE GuildID = {ctx.guild.id}")
		db.commit()
		await ctx.send(f"Done. {EnvVars.botname} will now log for this server in {channel}")

	@setup.command()
	async def stoplogging(self, ctx):
		db.execute(f"UPDATE guild SET LogChannel = 0 WHERE  GuildID = {ctx.guild.id}")
		db.commit()
		await ctx.send("Got it! I will stop logging to your log channel!")


def setup(client):
	client.add_cog(ServerSetup(client))
