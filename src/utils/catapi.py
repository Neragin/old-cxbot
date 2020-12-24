import requests

from utils import vars


def getcat():
	data = requests.get(f"https://api.thecatapi.com/v1/images/search?mime_types=gif?api_key={vars.EnvVars.catapi}").json()
	dictdata: dict = data[0]
	return dictdata["url"]
