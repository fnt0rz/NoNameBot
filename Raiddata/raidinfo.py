import os
import requests
import discord
import datetime

key= os.getenv('wowAuditKey')


def getRaidData():
  response = requests.get('https://wowaudit.com/v1/raids?include_past=false', headers={'Authorization':key})

  jsn = response.json()
  raids = jsn["raids"]

  return raids

def getNextRaids(numberOfRaids):

  raids = getRaidData()
  found = 0
  d = datetime.date.today()
  foundRaids = []

  while found < numberOfRaids:
    for raid in raids:
      if d.strftime("%Y-%m-%d") == raid["date"]:
        foundRaids.append(raid)        
        found =+ 1
    d = d + datetime.timedelta(days=1)
  
  return foundRaids
  
def getRoster():
  raidData = getNextRaidInfo()
  roster = createEmbeddedMessage(parseRaidRoster(raidData, getRaiders()), raidData)

  return roster

def getNextRaid():
  return getNextRaids(1)

def getNextRaidInfo():
  raidId = getNextRaid()[0]["id"]
  raidurl = "https://wowaudit.com/v1/raids/{0}".format(str(raidId))
  rstr = requests.get(raidurl, headers={'Authorization':key}).json()

  return rstr

def getRaiders():
  raiders = requests.get("https://wowaudit.com/v1/characters", headers={'Authorization':key}).json()

  return raiders


def parseRaidRoster(raidData, raiders):
  lst = []
  for boss in raidData["encounters"]:
    if boss["enabled"] == True:
      rlist = []
      for r in boss["selections"]:
        if r["selected"] == True:
          rname = findRaiderName(r["character_id"], raiders)
          rlist.append({"name": rname, "role": r["role"]})
      lst.append({"boss": boss["name"], "raiders": rlist})
  return lst

def findRaiderName(id, raiders):
  for r in raiders:
    if id == r["id"]:
      return r["name"]

def createRoster(raidlist):
  melee = []
  ranged = []
  healers = []
  tanks = []
  for c in raidlist:
    if c["raider"]["role"] == "Ranged":
      ranged.append(f"{c['raider']['name']} ({ c['selected'] })")
    if c["raider"]["role"] == "Melee":
      melee.append(f"{c['raider']['name']} ({ c['selected'] })")
    if c["raider"]["role"] == "Tank":
      tanks.append(f"{c['raider']['name']} ({ c['selected'] })")
    if c["raider"]["role"] == "Heal":
      healers.append(f"{c['raider']['name']} ({ c['selected'] })")

  roster = {
    "melee": formatString(melee),
    "ranged": formatString(ranged),
    "healers": formatString(healers),
    "tanks": formatString(tanks)
  }

  return roster 

def createRosterList(raidinfo):
  lst = []
  rst = []

  for boss in raidinfo:
    for r in boss["raiders"]:
      lst.append(r)

  for raider in lst:
    n = lst.count(raider)
    if {"raider": raider, "selected": n} not in rst:
      rst.append({"raider": raider, "selected": n})

  return rst

def createEmbeddedMessage(raidinfo, raidData):
  raidUrl = "https://wowaudit.com/eu/tarren-mill/noname/main/raids/{0}".format( raidData["id"])

  message= discord.Embed(description=f"Time: {raidData['start_time']} - {raidData['end_time']} **·** Difficulty: {raidData['difficulty']}", colour= discord.Color.green())
  message.set_author(name="Roster for {0} raid on {1}".format(raidData["instance"], raidData["date"]))
  message.add_field(name="\u200b", value="\u200b")

  roster = createRoster(createRosterList(raidinfo))

  if len(raidinfo) > 1:
    message.add_field(name=f"Current roster for { len(raidinfo)} bosses:", value="\u200b", inline=False)
  else: 
    message.add_field(name=f"Current roster for { raidinfo[0]['boss']}:", value="\u200b", inline=False)


  if len(roster["tanks"]) > 0:
    message.add_field(name=":shield: Tanks:", value=roster["tanks"], inline=False)
  else:
    addNoRaidersField(message, ":shield: Tanks:")
  if len(roster["healers"]) > 0:
    message.add_field(name=":green_heart: Healers:", value=roster["healers"], inline=False)
  else:
    addNoRaidersField(message, ":green_heart: Healers:")
  if len(roster["ranged"]) > 0:
    message.add_field(name=":archery: Ranged", value=roster["ranged"], inline=False)
  else:
    addNoRaidersField(message, ":archery: Ranged:")
  if len(roster["melee"]) > 0:
    message.add_field(name=":crossed_swords: Melee:", value=roster["melee"], inline=False)
  else:
    addNoRaidersField(message, ":crossed_swords: Melee:")

  if len(raidinfo) > 1:
    message.add_field(name="\u200B", value="_** More then 1 bosses are selected be sure to check the roster following the link below **_", inline=False)

  message.add_field(name="\u200B", value=f"**[Roster]({raidUrl})**", inline=False)
  message.set_footer(text="Brought to you by Chookity!")
  
  return message

def formatString(item):
  return ", ".join(item)

def addNoRaidersField(message, icon):
  message.add_field(name=icon, value="No players yet", inline=False)








