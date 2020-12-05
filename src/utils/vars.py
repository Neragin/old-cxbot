import os


class EnvVars:
	botname = os.environ.get('BOTNAME')
	hypixelKey = os.environ.get('HYPIXEL_API_KEY')
	dbpassword = os.environ.get("DBPASS")
	dbuser = os.environ.get("DBUSER")
	mongoserver = os.environ.get("MONGOSERVER")
	discordkey = os.environ.get('DISCORD_API_KEY')
	catapi = os.environ.get('CATAPIKEY')


class Styling:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
