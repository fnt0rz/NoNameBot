import json
import os
import requests


guildId = os.getenv('GuildId')
teamId = os.getenv('TeamId')


def login():
    login()


def queryApi():
  try:
    raidUrl = 'https://wowaudit.com/api/guilds/{0}/teams/{1}/raids'.format(
        guildId, teamId)
    response = requests.get(raidUrl)
    if response is not None:
        print(response)
        raidData = json.load(response)
        print(raidData)
  except:
    print("Error loading data")
