from discord.ext import commands

class GeneralCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  


def setup(bot):
  bot.add_cog(GeneralCommands(bot))