import Social.socialinteractions as social
from discord.ext import commands, tasks
from Social.channelbase import getSocialTimer
import asyncio

class EventTimers(commands.Cog):
  delay = 10
  def __init__(self, bot):
    self.bot = bot
    self.addEvents()
    
  @tasks.loop(minutes=1)
  async def socialInteraction(self):
    print("Loop started")
    print(f"next iteration: { self.socialInteraction.next_iteration}")
    t = int(getSocialTimer())
    if t != self.delay:
      print("Found change in delay")
      self.delay = t
      self.socialInteraction.change_interval(minutes=t)
      print("Waiting for delay")
      await asyncio.sleep(self.delay * 60)
      print("starting loop again")  
      return self.socialInteraction.restart()
    return await social.doRandomEvent(self.bot)
  

  @socialInteraction.before_loop
  async def before_SocialInteraction(self):
    await self.bot.wait_until_ready()

  def addEvents(self):
    self.socialInteraction.start()

def setup(bot):
  bot.add_cog(EventTimers(bot))
