import Raiddata.raidinfo

async def checkCommandFor(msg, client):
  if msg.content.startswith('$roster'):
    await returnRoster(msg, client)


async def returnRoster(msg, client):
  response = Raiddata.raidinfo.getRoster()
  await msg.channel.send(response)