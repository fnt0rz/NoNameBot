import discord
import os
from webserver import keep_alive
from message_commands import checkCommandFor


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents)


@client.event
async def on_ready():
  print('logged in as user {0}'.format(client.user))
  return await client.change_presence(activity=discord.Activity(type=1, name='World of Warcraft'))

@client.event
async def on_message(message):
  await checkCommandFor(message, client)


keep_alive()
client.run(os.getenv('TOKEN'))