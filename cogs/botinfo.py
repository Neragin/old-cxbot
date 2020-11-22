from discord.ext import commands
from discord.ext.commands import Cog, command
from termcolor import colored
import os
import psutil


class Botinfo(Cog):
	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		print(colored('hi cogs are online', 'green'))

	@command(name = "invitelink")
	async def invite(self, ctx):
		await ctx.send("https://discord.com/api/oauth2/authorize?client_id=718284261358174250&permissions=8&scope=bot is the invite link to the bot!")

	@command(name = "RAM", aliases = ["memoryview", "ram", "memory"])
	async def ram(self, ctx):
		await ctx.send(f"I am using {psutil.virtual_memory().percent}% which is equal to {psutil.virtual_memory().used}")

	@command(name = "CPU")
	async def cpu(self, ctx):
		await ctx.send(psutil.cpu_percent())
		await ctx.send(psutil.cpu_count())
		await ctx.send(psutil.cpu_freq())


def setup(client):
	client.add_cog(Botinfo(client))