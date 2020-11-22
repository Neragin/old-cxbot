from discord import Intents
import os
import logging
import discord
from discord.ext import commands
from termcolor import colored
from discord.ext.commands import CommandNotFound
botname = os.environ.get('BOTNAME')
client = commands.Bot(command_prefix = f'{botname} ')  # the prefix
Intents = Intents.all()


@client.event
async def on_ready():
	await client.change_presence(status = discord.Status.idle, activity = discord.Game('cx bot'))
	print(colored('bot is ready', 'green'))  # says when bot is ready


@client.event
async def on_connect():
	print(colored('bot is connected', 'green'))


@client.event
async def on_disconnect():
	print(colored('bot is disconnected', 'red'))


@client.command(hidden = True)
async def load(ctx, extension):
	if ctx.author.id == 308404126830559233:
		client.load_extension(f'cogs.{extension}')
		await ctx.send('loaded')


@client.command(hidden = True)
async def unload(ctx, extension):
	if ctx.author.id == 308404126830559233:
		client.unload_extension(f'cogs.{extension}')
		await ctx.send('unloaded')


@client.command(hidden = True)
async def reload(ctx, extension):
	if ctx.author.id == 308404126830559233:
		client.unload_extension(f'cogs.{extension}')
		client.load_extension(f'cogs.{extension}')


async def on_error(self, err, *args, **kwargs):
	if err == "on_command_error":
		await args[0].send("Something went wrong!")

	raise


@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("pass in the required arguments dumbo")
	# elif isinstance(error, CommandNotFound):
	# 	pass
	# elif hasattr(error, "original"):
	# 	raise error.original
	# else:
	# 	raise error

for filename in os.listdir('cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename = 'logs/discordapi.log', encoding = 'utf-8', mode = 'w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client.run(os.environ.get('DISCORD_API_KEY'))
