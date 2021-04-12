from discord.ext import commands
import Social.voting as voting

class GeneralCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot  

  @commands.command()
  @commands.guild_only()
  async def owners(self, ctx):
    await ctx.send('My owners are Archescent and fnt.')

  @commands.command(description="""
  Create a voting.
  Usage: $vote <end date> <"question">(make sure to use quotes) optional: <answer 1> <answer 2> <answer 3>
  """)
  @commands.guild_only() 
  async def vote(self, ctx, arg1, arg2, *args):
    if not (arg1 or arg2):
      return await voting.returnErrorMessage(ctx)
    await voting.validateVotingContext(ctx, arg1, arg2, args)


def setup(bot):
  bot.add_cog(GeneralCommands(bot))