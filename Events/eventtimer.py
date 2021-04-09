import Social.socialinteractions as social
from time import sleep
from discord.ext import tasks, commands


bot = commands.Bot('!')

@tasks.loop(minutes=10)
async def socialInteraction():
  print("adding social...")
  await social.doRandomEvent(client)

@socialInteraction.before_loop
async def before_SocialInteraction():
  print("waiting...")
  sleep(10)
  print("started...")


async def addEvents(c):
  global client
  client = c
  socialInteraction.start()

