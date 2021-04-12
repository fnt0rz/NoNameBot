import discord

yes_no_reactions = ["👍", "👎"]
multiple_choice_reactions = ["🇦","🇧","🇨"]

async def createVoteMessage(ctx, endDate, question):
  embed = discord.Embed(description=f"Voting ends at: { endDate} ", colour=discord.Color.gold())
  embed.set_author(name=f"A new vote has been started by { ctx.author.name }")
  embed.add_field(name="Question:", value=f"{ question }")

  msg = await ctx.send(embed=embed)
  for emoji in yes_no_reactions:
    await msg.add_reaction(emoji)

  await ctx.message.delete()



async def returnErrorMessage(ctx):
  await ctx.send(f"{ctx.author.mention}, invalid voting request. Please refer to `$help vote` for more info")

async def createMultiChoiceVote(ctx, endDate, question, options):
  embed = discord.Embed(description=f"Voting ends at: { endDate} ", colour=discord.Color.gold())
  embed.set_author(name=f"A new vote has been started by { ctx.author.name }")
  embed.add_field(name="Question:", value=f"{ question }")

  msg = await ctx.send(embed=embed)
  i = 0
  while i < (len(options)):
    await msg.add_reaction(multiple_choice_reactions[i])
    i += 1
  await ctx.message.delete()

def validateVotingContext(ctx, endDate, question, options):
  if not (endDate or question):
    return returnErrorMessage(ctx)
  if options:
    return createMultiChoiceVote(ctx, endDate, question, options)
  return createVoteMessage(ctx, endDate, question)

