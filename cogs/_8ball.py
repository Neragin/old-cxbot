import random

import discord
from discord import Embed
from discord.ext import commands
import random

from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('8ball cog is online')
    @commands.command(aliases=['8ball', 'eightball', ])
    async def _8ball(self, ctx, *, question):
        if ctx.author.id == 308404126830559233:
            responsesrigged = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
                               "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
                               "Signs point to yes.", ]
            embed = Embed(title="8ball", color=0x0088ff)
            embed.add_field(name="Question: ", value=f"{question}", inline=False)
            embed.add_field(name="Answer:", value=f"{random.choice(responsesrigged)}", inline=True)
            embed.set_footer(text="date")
            await ctx.send(embed=embed)
            # await ctx.send(f'Question: {question}\nAnswer: {random.choice(responsesrigged)}')
        else:
            responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
                         "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
                         "Signs point to yes.", "Reply hazy, try again.", "Ask again later.",
                         "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                         "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.",
                         "Very doubtful."]  # this list is the 20 answers in 8ball
            embed = Embed(title="8ball", color=0x0088ff)
            embed.add_field(name="Question: ", value=f"{question}", inline=False)
            embed.add_field(name="Answer:", value=f"{random.choice(responses)}", inline=True)
            embed.set_footer(text="date")
            await self.client.say(embed=embed)
            # embed = Embed(title="8ball")
            # embed.add_field(name="question")
            # await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')  # prints out a random choice

def setup(client):
    client.add_cog(Example(client))