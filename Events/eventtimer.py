import Social.socialinteractions as social
from discord.ext import commands, tasks
from Social.channelbase import getSocialTimer
from time import sleep


class EventTimers(commands.Cog):
  delay = 10

  def __init__(self, bot):
    self.bot = bot
    self.addEvents()
    self.setDelay()
    print(self.delay)
    

  @tasks.loop(minutes=delay)
  async def socialInteraction(self):
    await social.doRandomEvent(self.bot)

  @socialInteraction.before_loop
  async def before_SocialInteraction(self):
    await self.bot.wait_until_ready()
    sleep(self.delay * 60)

  def addEvents(self):
    self.socialInteraction.start()

  def setDelay(self):
    t = getSocialTimer()
    if not t:
      return
    self.delay = t
    

def setup(bot):
  bot.add_cog(EventTimers(bot))
