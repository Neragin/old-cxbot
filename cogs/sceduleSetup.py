import os
import re
import asyncio

from discord.ext import commands
from discord.ext.commands import Cog
from pymongo import MongoClient
from termcolor import colored
dbpassword = os.environ.get("DBPASS")
dbuser = os.environ.get("DBUSER")
mongoserver = os.environ.get("MONGOSERVER")
cluster = MongoClient(f"{mongoserver}personal?retryWrites=true&w=majority")


class scedules(Cog):

	def __init__(self, client):
		self.client = client

	@Cog.listener()
	async def on_ready(self):
		print(colored('cog is online', 'green'))

	@commands.command()
	async def scheduleSetup(self, ctx):
		db = cluster["personal"]
		collection = db["scheduledReminders"]
		valid = False
		amorpm = ""
		person = ctx.author.id

		def check(m):
			print(m)
			return m.content and m.channel == ctx.channel and ctx.author.id == m.author.id

		await ctx.send("Hello! I will setup reminders for you! These reminders will be DM'ed to you. We recommend setting up reminders in the DM's of the Bot. This feature is also in beta, so make sure to set an actual reminder somewhere else, because this probably wont work.")
		await ctx.send("We will begin by setting up the time for these reminders. Please type out the time in which you want to be reminded, in this format aa:bb:cc:dd(aa = hour, bb = minute, cc = AM/PM, dd = timezone)")
		timeinput = await self.client.wait_for('message', check = check, timeout = 60)
		time = "" + timeinput.content
		times = time.split(":")
		result = re.match("^(([1][0-2])|([0][1-9])):[0-5][0-9]:(AM|PM):(...)$", timeinput.content)
		await ctx.send(result)
		if result == timeinput.content:
			await ctx.send("your time that you passed in doesn't pass my regex. Because regex literally looks like an ancient egyptian inscription, contact CxFuzion if you think this is a mistake. The command will now exit")
			return
		await ctx.send("pass")
		post = {"_id": ctx.author.id, "person": person, "hour": times[0], "minutes": times[1], "clock": times[2], "timezone": times[3]}
		collection.insert_one(post)
def setup(client):
	client.add_cog(scedules(client))
