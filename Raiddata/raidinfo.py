import json
import os
import requests


key= os.getenv('wowAuditKey')


def getRaidData():
  response = requests.get('https://wowaudit.com/v1/raids?include_past=false', headers={'Authorization':key})

  jsn = response.json()
  raids = jsn["raids"]

  return raids

def getRoster():
  nextraid = getRaidData()[0]
  raidData = getNextRaidInfo(nextraid["id"])
  raiders = getRaiders()

  roster = createMessage(parseRaidRoster(raidData, raiders), raidData)

  return roster


def getNextRaidInfo(raidId):
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

def createMessage(raidlist, raidData):
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

  message = """ Roster for next raid on {4}:
  :shield:: {2}
  :green_heart:: {3} 
  :crossed_swords:: {0}
  :archery:: {1}
  """.format(formatString(melee), formatString(ranged), formatString(tanks), formatString(healers), raidData["date"])
  return message

def formatString(item):
  return ", ".join(item)









