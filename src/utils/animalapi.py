"""

"""
from aiohttp import request

from utils.vars import EnvVars


async def gifcat():
	"""
	:return
	"""
	url = "https://api.thecatapi.com/v1/images/search?mime_types=gif"
	headers = {
		"x-api-key": EnvVars.catapi
	}
	
	async with request("GET", url, headers = headers) as response:
		if response.status == 200:
			data = await response.json()
			datadict: dict = data[0]
			return datadict["url"]
		else:
			return f"API returned a {response.status}"


async def cat():
	"""
	:return
	"""
	url = "https://api.thecatapi.com/v1/images/search?mime_type=jpg"
	headers: dict = {
		"x-api-key": EnvVars.catapi
	}
	
	async with request("GET", url, headers = headers) as response:
		if response.status == 200:
			data = await response.json()
			datadict: dict = data[0]
			return datadict["url"]
		else:
			return f"API returned a {response.status}"
