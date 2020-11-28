import math

import requests

from utils.vars import EnvVars

solo = ['solo', '1v1v1v1v1v1v1v1', 'solos']
doubles = ['doubles', '2v2v2v2v2v2v2v2', 'double', ]
BASE = 10_000
GROWTH = 2_500
REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
REVERSE_CONST = REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2 = 2 / GROWTH
"""
Gets the hypixel level
"""


def getLevel(name: str):
	data = requests.get(f"https://api.hypixel.net/player?key={EnvVars.hypixelKey}&name={name}").json()
	if data["player"] is None:
		return None
	exp = int(data["player"]["networkExp"])  # This just gets the player experience from our data
	return math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * exp))  # This converts Hypixel EXP to a network level


def averagefkdr(name):
	url = f"https://api.hypixel.net/player?key={EnvVars.hypixelKey}&name={name}"
	res = requests.get(url)
	data = res.json()
	print(type(data))
	sum = round(int(data['player']['stats']['Bedwars']['final_kills_bedwars']) / int(data['player']['stats']['Bedwars']['final_deaths_bedwars']), 2)
	starcount = int(data['player']['achievements']['bedwars_level'])
	solokills = int(data['player']['stats']['Bedwars']['eight_one_kills_bedwars']) / int(data['player']['stats']['Bedwars']['eight_one_deaths_bedwars'])
	f = int(data['player']['stats']['Bedwars']['eight_two_kills_bedwars']) / int(data['player']['stats']['Bedwars']['eight_two_deaths_bedwars'])
	g = int(data['player']['stats']['Bedwars']['four_three_kills_bedwars']) / int(data['player']['stats']['Bedwars']['four_three_deaths_bedwars'])
	h = int(data['player']['stats']['Bedwars']['four_four_kills_bedwars']) / int(data['player']['stats']['Bedwars']['four_four_deaths_bedwars'])
	gf = solokills + f + g + h
	gf = gf / 4
	edsd = int(data['player']['stats']['Bedwars']['eight_one_wins_bedwars']) / int(data['player']['stats']['Bedwars']['eight_one_losses_bedwars'])
	fdsds = int(data['player']['stats']['Bedwars']['eight_two_wins_bedwars']) / int(data['player']['stats']['Bedwars']['eight_two_losses_bedwars'])
	gsd = int(data['player']['stats']['Bedwars']['four_three_wins_bedwars']) / int(data['player']['stats']['Bedwars']['four_three_losses_bedwars'])
	dfs = int(data['player']['stats']['Bedwars']['four_four_wins_bedwars']) / int(data['player']['stats']['Bedwars']['four_four_losses_bedwars'])
	coins = (data['player']['stats']['Bedwars']['coins'])
	rr = edsd + fdsds + gsd + dfs
	rr = rr / 4
	return sum, starcount, gf, rr, coins


"""
This function gets winrate based on gamemode.
params - data - the data from hypixel.net
returns - winrate
"""


def getBedwarsWinRate(data: dict, gamemode: str):
	apiGamemode = {
		'solo': 'eight_one_',
		'doubles': 'eight_two_',
		'threes': 'four_three_',
		'fours': 'four_four_',
		'four': 'two_four_',
		'all': '',
	}
	return round(data['player']['stats']['Bedwars'][f"{apiGamemode[gamemode]}wins_bedwars"] / data['player']['stats']['Bedwars'][f"{apiGamemode[gamemode]}losses_bedwars"], 2)


"""
This returns gets the fkdr based on gamemode
params - data - the data from Hypixel's api
returns - average fkdr
"""


def getBedwarsFinalKillDeath(data: dict, gamemode: str):
	apiGamemode = {
		'solo': 'eight_one_',
		'doubles': 'eight_two_',
		'threes': 'four_three_',
		'fours': 'four_four_',
		'four': 'two_four_',
		'all': '',
	}
	return round(data['player']['stats']['Bedwars'][f"{apiGamemode[gamemode]}final_kills_bedwars"] / data["player"]["stats"]["Bedwars"][f"{apiGamemode[gamemode]}final_deaths_bedwars"], 2)
