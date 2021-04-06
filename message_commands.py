import Raiddata.raidinfo

async def checkCommandFor(msg, client):
  if msg.content.startswith('$roster'):
    await returnRoster(msg, client)


async def returnRoster(msg, client):
  embed = Raiddata.raidinfo.getRoster()
  await msg.channel.send(embed=embed)
