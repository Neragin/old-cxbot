"""
backend code for hypixel commands
"""
import math

import requests

from utils.vars import EnvVars

solo: list = ['solo', '1v1v1v1v1v1v1v1', 'solos']
doubles: list = ['doubles', '2v2v2v2v2v2v2v2', 'double', ]
BASE: int = 10_000
GROWTH: int = 2_500
REVERSE_PQ_PREFIX: float = -(BASE - 0.5 * GROWTH) / GROWTH
REVERSE_CONST: float = REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2: float = 2 / GROWTH
BEDWARS_EXP_PER_PRESTIGE: int = 489000
BEDWARS_LEVELS_PER_PRESTIGE: int = 100


def get_level(name: str) -> float or None:
	"""
	This function gets the hypixel level of a username
	:param name: the name of the player
	:return: the level of the player
	"""
	data = requests.get(f"https://api.hypixel.net/player?key={EnvVars.hypixelKey}&name={name}").json()
	if data["player"] is None:
		return None
	exp = int(data["player"]["networkExp"])  # This just gets the player experience from our data
	return math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * exp))  # This converts Hypixel EXP to a network level


def get_star(data: dict) -> float or int:
	"""
	This function returns the star of the hypixel player
	:param data: the hypixel api in a dictionary format
	:return: the star of the player specified in the data
	"""
	exp = data['player']['stats']['Bedwars']['Experience']
	
	prestige = round(exp / BEDWARS_EXP_PER_PRESTIGE)
	exp %= BEDWARS_EXP_PER_PRESTIGE
	if prestige > 5:
		over = prestige % 5
		exp += over * BEDWARS_EXP_PER_PRESTIGE
		prestige -= over
	if exp < 500:
		return prestige * BEDWARS_LEVELS_PER_PRESTIGE
	elif exp < 1500:
		return 1 + (prestige * BEDWARS_LEVELS_PER_PRESTIGE)
	elif exp < 3500:
		return 2 + (prestige * BEDWARS_LEVELS_PER_PRESTIGE)
	elif exp < 5500:
		return 3 + (prestige * BEDWARS_LEVELS_PER_PRESTIGE)
	elif exp < 9000:
		return 4 + (prestige * BEDWARS_LEVELS_PER_PRESTIGE)
	exp -= 9000
	return (exp / 5000 + 4) + (prestige * BEDWARS_LEVELS_PER_PRESTIGE)


def get_bedwars_win_rate(data: dict, gamemode: str) -> int:
	"""
	This function gets the bedwars win rate based on the player in data
	:param data: the data in hypixel's api
	:param gamemode: the gamemode to get for
	:return: the win rate
	"""
	api_gamemode = {
		'solo': 'eight_one_',
		'doubles': 'eight_two_',
		'threes': 'four_three_',
		'fours': 'four_four_',
		'four': 'two_four_',
		'all': '',
	}
	return round(data['player']['stats']['Bedwars'][f"{api_gamemode[gamemode]}wins_bedwars"] / data['player']['stats']['Bedwars'][f"{api_gamemode[gamemode]}losses_bedwars"], 2)


def get_bedwars_fkdr(data: dict, gamemode: str) -> int:
	"""
	This function gets the bedwars final kdr based on the player in data
	:param data: the data from hypixel
	:param gamemode: the gamemode to get for
	:return: the final kill death ratio of the player
	"""
	api_gamemode = {
		'solo': 'eight_one_',
		'doubles': 'eight_two_',
		'threes': 'four_three_',
		'fours': 'four_four_',
		'four': 'two_four_',
		'all': '',
	}
	return round(data['player']['stats']['Bedwars'][f"{api_gamemode[gamemode]}final_kills_bedwars"] / data["player"]["stats"]["Bedwars"][f"{api_gamemode[gamemode]}final_deaths_bedwars"], 2)
