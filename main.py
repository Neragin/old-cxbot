import os

import discord
from discord.ext import commands
botname = os.environ.get('BOTNAME')
client = commands.Bot(command_prefix=f'{botname} ')  # the prefix


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('cx bot'))
    print('bot is ready')  # says when bot is ready


@client.command(hidden=True)
async def load(ctx, extension):
    if ctx.author.id == 308404126830559233:
        client.load_extension(f'cogs.{extension}')
        await ctx.send('loaded')


@client.command(hidden=True)
async def unload(ctx, extension):
    if ctx.author.id == 308404126830559233:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send('unloaded')


@client.command(hidden=True)
async def reload(ctx, extension):
    if ctx.author.id == 308404126830559233:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
client.run(os.environ.get('DISCORD_API_KEY'))
