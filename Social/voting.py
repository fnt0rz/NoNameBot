import discord

yes_no_reactions = ["👍", "👎"]
multiple_choice_reactions = ["🇦","🇧","🇨"]

async def createVoteMessage(ctx, *args):
  print(args)
  embed = discord.Embed(description="Voting ends at: ", colour=discord.Color.gold())
  embed.set_author(name=f"A new vote has been started by { ctx.author.name }")
  embed.add_field(name=f"{ args[0] }", value="Options here")

  msg = await ctx.send(embed=embed)
  for emoji in multiple_choice_reactions:
    await msg.add_reaction(emoji)
  

