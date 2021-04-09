from discord.ext import commands
import Social.channelbase as channelbase

class AdminCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def setChannel(self, ctx):
    await channelbase.setGeneralChannel(ctx)

  @commands.command()
  async def getChannel(self, ctx):
    await channelbase.getGeneralChannel(ctx, self.bot)


def setup(bot):
  bot.add_cog(AdminCommands(bot))