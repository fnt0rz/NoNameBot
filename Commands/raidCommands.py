import Raiddata.raidinfo
from discord.ext import commands

class RaidCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(description='Get the roster of next raid')
  async def roster(self, ctx):
    await self.returnRoster(ctx)

  async def returnRoster(self, ctx):
    embed = Raiddata.raidinfo.getRoster()
    await ctx.channel.send(embed=embed)


def setup(bot):
  bot.add_cog(RaidCommands(bot))


