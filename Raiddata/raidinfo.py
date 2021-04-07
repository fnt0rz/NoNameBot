import os
import requests
import discord


key= os.getenv('wowAuditKey')


def getRaidData():
  response = requests.get('https://wowaudit.com/v1/raids?include_past=false', headers={'Authorization':key})

  jsn = response.json()
  raids = jsn["raids"]

  return raids

def getNextRaid():
  return getRaidData()[0]
  
def getRoster():
  raidData = getNextRaidInfo()
  roster = createEmbeddedMessage(parseRaidRoster(raidData, getRaiders()), raidData)

  return roster


def getNextRaidInfo():
  raidId = getNextRaid()["id"]
  raidurl = "https://wowaudit.com/v1/raids/{0}".format(str(raidId))
  rstr = requests.get(raidurl, headers={'Authorization':key}).json()

  return rstr

def getRaiders():
  raiders = requests.get("https://wowaudit.com/v1/characters", headers={'Authorization':key}).json()

  return raiders


def parseRaidRoster(raidData, raiders):
  lst = []
  for r in raidData["signups"]:
    if r["selected"] == True:
      lst.append(r)
  return lst

def createRoster(raidlist):
  melee = []
  ranged = []
  healers = []
  tanks = []

  for c in raidlist:
    if c["role"] == "Ranged":
      ranged.append(c["character"]["name"])
    if c["role"] == "Melee":
      melee.append(c["character"]["name"])
    if c["role"] == "Tank":
      tanks.append(c["character"]["name"])
    if c["role"] == "Heal":
      healers.append(c["character"]["name"])

  roster = {
    "melee": formatString(melee),
    "ranged": formatString(ranged),
    "healers": formatString(healers),
    "tanks": formatString(tanks)
  }

  return roster 

def createEmbeddedMessage(raidinfo, raidData):
  roster = createRoster(raidinfo)
  print(roster)
  footerNote = "Total sign-ups: {0} · brought to you by Chookity!".format(str(len(raidData["signups"])))

  raidUrl = "https://wowaudit.com/eu/tarren-mill/noname/main/raids/{0}".format( raidData["id"])

  message= discord.Embed(description="Roster for _**{0}**_ raid on _**{1}**_".format(raidData["instance"], raidData["date"]), colour= discord.Color.green())
  message.set_author(name="Raid Roster")
  message.add_field(name="\u200b", value="\u200b")

  if len(roster["tanks"]) > 0:
    message.add_field(name=":shield: Tanks", value=roster["tanks"], inline=False)
  else:
    addNoRaidersField(message, ":shield: Tanks")
  if len(roster["healers"]) > 0:
    message.add_field(name=":green_heart: Healers", value=roster["healers"], inline=False)
  else:
    addNoRaidersField(message, ":green_heart: Healers")
  if len(roster["ranged"]) > 0:
    message.add_field(name=":archery: Ranged", value=roster["ranged"], inline=False)
  else:
    addNoRaidersField(message, ":archery: Ranged")
  if len(roster["melee"]) > 0:
    message.add_field(name=":crossed_swords: Melee", value=roster["melee"], inline=False)
  else:
    addNoRaidersField(message, ":crossed_swords: Melee")
  message.add_field(name="\u200B", value=f"**[Roster]({raidUrl})**")
  message.set_footer(text=footerNote)
  
  return message

def formatString(item):
  return ", ".join(item)

def addNoRaidersField(message, icon):
  message.add_field(name=icon, value="No players yet", inline=False)









