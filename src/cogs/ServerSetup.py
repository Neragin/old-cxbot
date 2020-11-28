from discord import TextChannel
from discord.ext import commands
from pymongo import MongoClient

from utils.vars import EnvVars

cluster = MongoClient(f"{EnvVars.mongoserver}GuildData?retryWrites=true&w=majority")


class ServerSetup(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.group(invoke_without_command = True)
	async def setup(self, ctx):
		await ctx.send(f"Hello! I am the wizard for {EnvVars.botname} bot. This command is for a group of commands, so use {EnvVars.botname} setup <command>")

	@setup.command()
	async def logging(self, ctx, channel: TextChannel):
		db = cluster["Bot"]
		collection = db["GuildData"]
		await ctx.send("Good to go!")
		await ctx.send(channel)
		if type(channel) == TextChannel and channel.guild == ctx.guild:
			await ctx.send("yes")
		else:
			await ctx.send("That either isn't a valid channel(hint: use #channelname), or that channel isn't in this server")
		post = {"_id": ctx.guild.id, "logs": channel.id}
		collection.insert_one(post)

	@setup.command()
	async def stoplogging(self, ctx):
		db = cluster["Bot"]
		collection = db["GuildData"]
		logchannel = collection.find_one({"_id": ctx.guild.id})
		print(logchannel["logs"])
		result = collection.update_one({"_id": ctx.guild.id}, {"$unset": {"logs": logchannel["logs"]}})
		print(result)


def setup(client):
	client.add_cog(ServerSetup(client))
