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