from io import BytesIO

from PIL import Image


async def getimg(imglink, tag):
	"""
	bot moment
	:param imglink:
	:param tag:
	"""
	asset = imglink
	data = BytesIO(await asset.read)
	pfp = Image.open(data)
	pfp.save("/data/images/{tag}.png", "PNG")
