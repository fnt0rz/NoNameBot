import Social.channelbase as channelbase
from random import randrange
from time import sleep

async def doRandomEvent(client):
  c = getChannel(client)

  if not c:
    return

  u = getRandomUser(c)
  r = randrange(100)
  await fireEvent(c, u, r)

async def fireEvent(c, u ,r):
  print(f"Rolled { r }")
  if r > 95:
    await c.send("Warrior Mooncake is ready for battle...")
    await c.send("10, 9, 8, 7, 6, 5, 4, 3, 2, 1, **GO!**")
    return await c.send("Charge -> Colossus Smash -> Mortal Strike -> Overpower -> Condemn -> Condemn -> Condemn -> Condemn -> Condemn -> Condemn -> Condemn -> Condemn -> Condemn")
  if r > 92:
    await c.send("$sim Mooncake")
    await c.send("Waiting for api...")
    sleep(5)
    return await c.send("WHAT! Its over 9000!")
  if r > 90:
    message = await c.send(f"Please help me summon { u.name }!")
    return await message.add_reaction("✋")
  if r > 80:
    return await c.send(f"Power Infusion cast on { u.name}, go brrrrrr!")
  if r > 75:
    return await c.send("Warlock Mooncake is handing out fel cookies")
  if r > 70:
    anima = randrange(7000)
    return await c.send(f"Mooncake steals { anima } anima from { u } ")


def getRandomUser(c):
  nr = randrange(len(c.members))
  return  c.members[nr]

def getChannel(client):
  cid = channelbase.getGeneralChannelId()
  return client.get_channel(cid)