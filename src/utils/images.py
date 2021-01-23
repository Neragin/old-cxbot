from os import listdir
from os.path import splitext

PATH = "data/images"


async def getimgs(imgtag):
	dirs = listdir(PATH)
	print("starting getimg stuff")
	for file in dirs:
		print(file)
		if splitext(file)[0] == imgtag:
			print(file)
			return file
