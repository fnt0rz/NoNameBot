import discord, os
from discord.ext import commands
from webserver import keep_alive

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

extensions = [
    'Commands.adminCommands', 'Commands.generalCommands',
    'Commands.raidCommands', 'Events.eventtimer'
]

if __name__ == '__main__':
	for ext in extensions:
		bot.load_extension(ext)


@bot.event
async def on_ready():
	print('logged in as user {0}'.format(bot.user))
	await bot.change_presence(
	    activity=discord.Activity(type=1, name='World of Warcraft'))


def getClient():
	return bot


keep_alive()
bot.run(os.getenv('TOKEN'), bot=True, reconnect=True)
