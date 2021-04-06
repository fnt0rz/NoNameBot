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

@client.event
async def on_member_join(member):
  print('{0} joined the server'.format(member.name))
  channel = client.get_channel(820241232222748692)
  await channel.send('Hello {0}!'.format(member.name))

@client.event
async def on_message(message):
  await checkCommandFor(message, client)


keep_alive()
client.run(os.getenv('TOKEN'))