import discord
import random
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)


# This is a decorator that defines a function as a bot command.
@bot.command() 
async def ping(ctx):
	"""
	This defines a command named "ping" that takes one parameter, ctx, which is the context.
	represents the context in which a command is invoked and provides information about the message, 
	the user who triggered the command, the channel where the command was used, and more.
	"""
	await ctx.send("pong!")

@bot.command()
async def coinflip(ctx):
	"""
	This defines a command named "coinflip" that takes ctx as a parameter.
	It randomly returns either heads or tails when called in a disord server.
	"""
	num = random.randint(1,2)
	if num == 1:
		await ctx.send("heads!")
	if num == 2:
		await ctx.send("tails!")

# WITH EMOJIS
# @bot.command()
# async def rps(ctx, hand):
# 	"""
#     Play Rock-Paper-Scissors with the bot.

#     Parameters:
#     - hand (str): The player's chosen hand ("✌️" for scissors, "👊" for rock, "✋" for paper).

#     Example:
#     !rps ✌️
#     """
# 	hands = ["✌️", "👊", "✋"]
# 	botHand = random.choice(hands)
# 	await ctx.send(botHand)
# 	if hand == botHand:
# 		await ctx.send("its a draw!")
# 	elif hand == "✌️":
# 		if botHand == "👊":
# 			await ctx.send("I won!")
# 		if botHand == "✋":
# 			await ctx.send("You won!")
# 	elif hand == "👊":
# 		if botHand == "✌️":
# 			await ctx.send("You won!")
# 		if botHand == "✋":
# 			await ctx.send("I won!")
# 	elif hand == "✋":
# 		if botHand == "✌️":
# 			await ctx.send("I won!")
# 		if botHand == "👊":
# 			await ctx.send("You won!")

# WITH WORDS
@bot.command()
async def rps(ctx, hand):
    """
    Play Rock-Paper-Scissors with the bot.

    Parameters:
    - hand (str): The player's chosen hand ("scissors", "rock", "paper").

    Example:
    !rps scissors
    """
    hands = ["scissors", "rock", "paper"]

    # Bot randomly chooses a hand
    bot_hand = random.choice(hands)

    # Send the bot's chosen hand as a response
    await ctx.send(f"I choose: {bot_hand}")

    # Determine the winner
    if hand == bot_hand:
        await ctx.send("It's a draw!")
    elif hand == "scissors":
        if bot_hand == "rock":
            await ctx.send("I won!")
        elif bot_hand == "paper":
            await ctx.send("You won!")
    elif hand == "rock":
        if bot_hand == "scissors":
            await ctx.send("You won!")
        elif bot_hand == "paper":
            await ctx.send("I won!")
    elif hand == "paper":
        if bot_hand == "scissors":
            await ctx.send("I won!")
        elif bot_hand == "rock":
            await ctx.send("You won!")


























bot.run("MTE4NzYyOTkwMTkyNzQzNjMzOA.GJOdwU.D-lcgjihXqGWzaiaFwGJw4QvkKgZhRd3xAQXpY")