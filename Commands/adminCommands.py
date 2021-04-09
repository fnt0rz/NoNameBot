from discord.ext import commands
import Social.channelbase as channelbase

class AdminCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(hidden=True)
  async def setChannel(self, ctx):
    await channelbase.setGeneralChannel(ctx)

  @commands.command(hidden=True)
  async def getChannel(self, ctx):
    await channelbase.getGeneralChannel(ctx, self.bot)

  @commands.command(hidden=True)
  async def setDelay(self, ctx, delay: str):
    result = channelbase.setSocialTimer(delay)
    await ctx.send(result)

  @commands.command(hidden=True)
  async def getDelay(self, ctx):
    result = channelbase.getSocialTimerText()
    await ctx.send(result)


def setup(bot):
  bot.add_cog(AdminCommands(bot))