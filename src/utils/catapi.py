import requests

from utils import vars


def getCat():
	data = requests.get(f"https://api.thecatapi.com/v1/images/search?mime_types=gif?api_key={vars.EnvVars.catapi}").json()
	dictdata = data[0]
	return dictdata["url"]
