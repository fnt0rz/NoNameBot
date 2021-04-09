import Social.channelbase as channelbase
from random import randrange

async def doRandomEvent(client):
  c = getChannel(client)

  if not c:
    return

  u = getRandomUser(c)
  r = randrange(100)
  await fireEvent(c, u, r)

async def fireEvent(c, u ,r):
  print(f"Rolled { r }")
  if r > 90:
    message = await c.send(f"Please help me summon { u.name }!")
    return await message.add_reaction("✋")
  if r > 80:
    return await c.send(f"Power Infusion cast on { u.name}, go brrrrrr!")

def getRandomUser(c):
  nr = randrange(len(c.members))
  return  c.members[nr]

def getChannel(client):
  cid = channelbase.getGeneralChannelId()
  return client.get_channel(cid)