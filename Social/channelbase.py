from replit import db

async def setGeneralChannel(msg):
    c = msg.channel
    result = setGeneralChannelId(c.id)
    if result == True:
      return await msg.channel.send(f"Chookity-pah, { c.mention } is now set as general channel.")
    else: 
      return await msg.channel.send("Failed to set channel")

async def getGeneralChannel(msg, bot):
  cid = getGeneralChannelId()
  if not cid:
    return await msg.channel.send("Not channel set yet, try using $setChannel")
  
  c = bot.get_channel(cid)
  if not c:
    return await msg.channel.send("Not channel set yet, try using $setChannel")

  return await msg.channel.send(f"Chookity-Chook, { c.mention } is currently set as general channel.")

def getSocialTimerText():
  return f"Chookity-Chook, { getSocialTimer() } minutes is currently set as delay."

def setSocialTimer(minutes):
  db["socialTimer"] = minutes
  return f"Chookity-pah, delay is now set to {minutes} minutes."

def getSocialTimer():
  return db["socialTimer"]

def setGeneralChannelId(id):
  db["generalChannel"] = id
  return True

def getGeneralChannelId():
  return db["generalChannel"]