"""

"""
import os

import discord
from discord.ext import commands
from discord.ext.commands import command, Cog

from utils import data as db, images


class Owner(Cog):
	"""

	"""
	
	def __init__(self, client):
		self.client = client
	
	@command(name = "speak", hidden = True)
	@commands.is_owner()
	async def speak(self, ctx, getchannel: str, *, message: str):
		channel = self.client.get_channel(int(getchannel))
		await channel.send(message)
	
	@speak.error
	async def speak_error(self, ctx, error: discord.ext.commands.CommandError):
		"""

		:param error:
		"""
		if isinstance(error, commands.CheckFailure):
			await ctx.send("You aren't my Owner!")
		else:
			raise error
	
	@command(name = "shutdown", aliases = ["die", "kill", "terminate", "disconnect", "exit", "goboom"])
	@commands.is_owner()
	async def shutdown(self, ctx):
		await ctx.send("I am shutting down now.")
		await self.client.change_presence(status = discord.Status.do_not_disturb, activity = discord.Game("Shutting down!"))
		db.close()
		await self.client.close()
	
	@command(hidden = True)
	@commands.is_owner()
	async def load(self, ctx, extension):
		self.client.load_extension(f'cogs.{extension}')
		await ctx.send('loaded')
	
	@command(hidden = True)
	@commands.is_owner()
	async def unload(self, ctx, extension):
		if ctx.author.id == 308404126830559233:
			self.client.unload_extension(f'cogs.{extension}')
			await ctx.send(f'unloaded {extension}')
	
	@command(hidden = True)
	@commands.is_owner()
	async def reload(self, ctx, extension):
		self.client.unload_extension(f'cogs.{extension}')
		self.client.load_extension(f'cogs.{extension}')
		await ctx.send(f"reloaded {extension}")
	
	@commands.group(name = "image", aliases = ["img"], invoke_without_command = True)
	@commands.is_owner()
	async def img(self, ctx):
		await ctx.send("this is a group of commands u tard")
	
	@img.command()
	@commands.is_owner()
	async def upload(self, ctx, name: str = None):
		"""
		uploads an image to cxbot
		"""
		await ctx.send("okay, send in a image")
		
		msg: discord.Message = await self.client.wait_for('message')
		msg: discord.Attachment = msg.attachments[0]
		split = os.path.splitext(msg.filename)
		print(split)
		await msg.save(f"data/images/{msg.filename if name is None else name + split[1]}")
	
	@img.command()
	@commands.is_owner()
	async def get(self, ctx, imgtag):
		img = await images.getimgs(imgtag)
		print(img)
		# print(type(img))
		await ctx.send(file = discord.File(f'data/images/{img}'))


def setup(client):
	client.add_cog(Owner(client))
