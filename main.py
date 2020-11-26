import logging
import os

from discord import Intents
from discord.ext.commands import Bot
from termcolor import colored
from utils import ApiLogging

botname = os.environ.get('BOTNAME')

client = Bot(command_prefix = f"{botname} ")  # the prefix
Intents = Intents.all()


@client.event
async def on_ready():
	print(colored('bot is ready', 'green'))  # says when bot is ready


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


for filename in os.listdir('cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

ApiLogging.apilogging()
client.run(os.environ.get('DISCORD_API_KEY'))
