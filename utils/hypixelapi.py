import math
import requests
import time
import os
import datetime
api_key = os.environ.get('HYPIXEL_API_KEY')
solo = ['solo', '1v1v1v1v1v1v1v1', 'solos']
doubles = ['doubles', '2v2v2v2v2v2v2v2', 'double', ]
BASE = 10_000
GROWTH = 2_500
REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
REVERSE_CONST = REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2 = 2 / GROWTH

def get_level(name):
    url = f"https://api.hypixel.net/player?key={api_key}&name={name}"
    res = requests.get(url)
    data = res.json()
    if data["player"] is None:
        return None
    exp = int(data["player"]["networkExp"]) # This just gets the player experience from our data
    return math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * exp)) # This converts Hypixel EXP to a network level

def averagefkdr(name):
    url = f"https://api.hypixel.net/player?key={api_key}&name={name}"
    res = requests.get(url)
    data = res.json()
    sum = round(int(data['player']['stats']['Bedwars']['final_kills_bedwars']) / int(data['player']['stats']['Bedwars']['final_deaths_bedwars']), 2)
    starcount = int(data['player']['achievements']['bedwars_level'])
    e = int(data['player']['stats']['Bedwars']['eight_one_kills_bedwars']) / int(data['player']['stats']['Bedwars']['eight_one_deaths_bedwars'])
    f = int(data['player']['stats']['Bedwars']['eight_two_kills_bedwars']) / int(data['player']['stats']['Bedwars']['eight_two_deaths_bedwars'])
    g = int(data['player']['stats']['Bedwars']['four_three_kills_bedwars']) / int(data['player']['stats']['Bedwars']['four_three_deaths_bedwars'])
    h = int(data['player']['stats']['Bedwars']['four_four_kills_bedwars']) / int(data['player']['stats']['Bedwars']['four_four_deaths_bedwars'])
    gf = e + f + g + h
    gf = gf / 4
    edsd = int(data['player']['stats']['Bedwars']['eight_one_wins_bedwars']) / int(data['player']['stats']['Bedwars']['eight_one_losses_bedwars'])
    fdsds = int(data['player']['stats']['Bedwars']['eight_two_wins_bedwars']) / int(data['player']['stats']['Bedwars']['eight_two_losses_bedwars'])
    gsd = int(data['player']['stats']['Bedwars']['four_three_wins_bedwars']) / int(data['player']['stats']['Bedwars']['four_three_losses_bedwars'])
    dfs = int(data['player']['stats']['Bedwars']['four_four_wins_bedwars']) / int(data['player']['stats']['Bedwars']['four_four_losses_bedwars'])
    coins = (data['player']['stats']['Bedwars']['coins'])
    rr = edsd + fdsds + gsd + dfs
    rr = rr / 4
    return sum, starcount, gf, rr, coins

