from discord.ext import commands

class GeneralCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot  

  @commands.command()
  @commands.guild_only()
  async def owners(self, ctx):
    await ctx.send('My owners are Archescent and fnt.')


def setup(bot):
  bot.add_cog(GeneralCommands(bot))