import discord
import random
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", help_command = None, intents = intents)


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

@bot.command(aliases = ["about"])
async def help(ctx):
    """
    Command to display information about available bot commands.

    Parameters:
        ctx (commands.Context): The context in which the command was invoked.

    Usage:
        !help or !about
    """
    # Create an embedded message with information about commands
    myEmbed = discord.Embed(
        title="Commands",
        description="These are the commands that you can use for this bot.",
        color=discord.Color.dark_purple()
    )
    myEmbed.set_thumbnail(url="https://i.pinimg.com/736x/ce/5c/ee/ce5cee4b4eab5058e858cbf8b65c39a4.jpg")
    myEmbed.add_field(name="!ping", value="This command replies back with pong whenever you write !ping.", inline=False)
    myEmbed.add_field(name="!coinflip", value="This command lets you flip a coin.", inline=False)
    myEmbed.add_field(name="!rps", value="This command allows you to play a game of rock paper scissors with the bot.", inline=False)

    # Send the embedded message to the channel where the command was invoked
    await ctx.send(embed=myEmbed)

@bot.group()
async def edit(ctx):
    """
    Group of commands for editing server-related settings.

    Usage:
        !edit servername <new_server_name>
        !edit region <new_region>
        !edit createtextchannel <channel_name>
        !edit createvoicechannel <channel_name>
        !edit createrole <role_name>
    """
    pass

@edit.command()
async def servername(ctx, *, input):
    """
    Command to change the server's name.

    Parameters:
        ctx (commands.Context): The context in which the command was invoked.
        input (str): The new server name.

    Usage:
        !edit servername <new_server_name>
    """
    await ctx.guild.edit(name=input)
    await ctx.send(f"Server name changed to '{input}'.")

@edit.command()
async def region(ctx, *, input):
    """
    Command to change the server's region.

    Parameters:
        ctx (commands.Context): The context in which the command was invoked.
        input (str): The new server region.

    Usage:
        !edit region <new_region>
    """
    await ctx.guild.edit(rtc_region=input)
    await ctx.send(f"Server region changed to '{input}'.")

@edit.command()
async def createtextchannel(ctx, *, input):
    """
    Command to create a text channel within a specific category.

    Parameters:
        ctx (commands.Context): The context in which the command was invoked.
        input (str): The name of the text channel to be created.

    Usage:
        !edit createtextchannel <channel_name>
    """
    # Find or create the category by name
    category_name = "new channels"
    category = discord.utils.get(ctx.guild.categories, name=category_name)
    if category is None:
        category = await ctx.guild.create_category(category_name, position=0)
        await ctx.send(f"Category '{category_name}' created.")

    # Create a text channel within the specified category
    await ctx.guild.create_text_channel(name=input, category=category)
    await ctx.send(f"Text channel '{input}' created in category '{category_name}'.")

@edit.command()
async def createvoicechannel(ctx, *, input):
    """
    Command to create a voice channel within a specific category.

    Parameters:
        ctx (commands.Context): The context in which the command was invoked.
        input (str): The name of the voice channel to be created.

    Usage:
        !edit createvoicechannel <channel_name>
    """
    # Find or create the category by name
    category_name = "new voice channels"
    category = discord.utils.get(ctx.guild.categories, name=category_name)
    if category is None:
        category = await ctx.guild.create_category(category_name, position=10)
        await ctx.send(f"Category '{category_name}' created.")

    # Create a voice channel within the specified category
    await ctx.guild.create_voice_channel(name=input, category=category)
    await ctx.send(f"Voice channel '{input}' created in category '{category_name}'.")

@edit.command()
async def createrole(ctx, *, input):
    """
    Command to create a new role.

    Parameters:
        ctx (commands.Context): The context in which the command was invoked.
        input (str): The name of the role to be created.

    Usage:
        !edit createrole <role_name>
    """
    await ctx.guild.create_role(name=input)
    await ctx.send(f"Role '{input}' has been created.")

@bot.command()
async def kick(ctx, user: int, *, reason=None):
    """
    Command to kick a user from the server.

    Parameters:
        - ctx (commands.Context): The context of the command.
        - user (int): The ID of the user to kick.
        - reason (str): Optional reason for kicking the user.

    Usage: !kick <user_id> [reason]
    """
    # Get the Member object using the user ID
    member = ctx.guild.get_member(user)
    
    # Check if the member is found in the guild
    if member is None:
        await ctx.send("User not found.")
    else:
        # Kick the member
        await member.kick(reason=reason)
        await ctx.send(f'Successfully kicked {member.name}#{member.discriminator}')

@bot.command()
async def ban(ctx, user: int, *, reason=None):
    """
    Command to ban a user from the server.

    Parameters:
        - ctx (commands.Context): The context of the command.
        - user (int): The ID of the user to ban.
        - reason (str): Optional reason for banning the user.

    Usage: !ban <user_id> [reason]
    """
    # Get the Member object using the user ID
    member = ctx.guild.get_member(user)
    
    # Check if the member is found in the guild
    if member is None:
        await ctx.send("User not found.")
    else:
        # Ban the member
        await member.ban(reason=reason)
        await ctx.send(f'Successfully banned {member.name}#{member.discriminator}')

@bot.command()
async def unban(ctx, user: int):
    """
    Command to unban a user from the server.

    Parameters:
        - ctx (commands.Context): The context of the command.
        - user (int): The ID of the user to unban.

    Usage: !unban <user_id>
    """
    try:
        # Fetch the user object using the user ID
        member = await bot.fetch_user(user)
        
        # Unban the user
        await ctx.guild.unban(member)
        await ctx.send(f"Successfully unbanned {member.name}")
    except discord.NotFound:
        await ctx.send("User not found.")

@bot.command()
async def purge(ctx, amount, day: int = None, month: int = None, year: int = datetime.now().year):
    """
    Command to delete messages from the channel.

    Parameters:
        - ctx (commands.Context): The context of the command.
        - amount (int or str): The number of messages to delete or '/' to delete messages after a specific date.
        - day (int): The day for filtering messages (only applicable if amount is '/').
        - month (int): The month for filtering messages (only applicable if amount is '/').
        - year (int): The year for filtering messages (only applicable if amount is '/').

    Usage:
        - To delete a specific number of messages: !purge <amount>
        - To delete messages after a specific date: !purge / <day> <month> <year>
    """
    if amount == "/":
        # Check if day and month are provided for date-based purging
        if day is None or month is None:
            return
        else:
            # Purge messages after the specified date
            await ctx.channel.purge(after=datetime(year, month, day))
            await ctx.send(f"Texts after {day}/{month}/{year} have been deleted!")
    else:
        # Purge the specified number of messages
        await ctx.channel.purge(limit=int(amount) + 1)
        await ctx.send(f"Previous {amount} texts have been deleted!")

@bot.command()
async def mute(ctx, user: discord.Member):
    """
    Command to mute a user in the voice channel.

    Parameters:
        - ctx (commands.Context): The context of the command.
        - user (discord.Member): The member to be muted.

    Usage: !mute <user_mention>
    """
    await user.edit(mute=True)
    await ctx.send(f"{user.display_name} has been muted in the voice channel.")

@bot.command()
async def unmute(ctx, user: discord.Member):
    """
    Command to unmute a user in the voice channel.

    Parameters:
        - ctx (commands.Context): The context of the command.
        - user (discord.Member): The member to be unmuted.

    Usage: !unmute <user_mention>
    """
    await user.edit(mute=False)
    await ctx.send(f"{user.display_name} has been unmuted in the voice channel.")

@bot.command()
async def deafen(ctx, user: discord.Member):
    """
    Command to deafen a user in the voice channel.

    Parameters:
        - ctx (commands.Context): The context of the command.
        - user (discord.Member): The member to be deafened.

    Usage: !deafen <user_mention>
    """
    await user.edit(deafen=True)
    await ctx.send(f"{user.display_name} has been deafened in the voice channel.")

@bot.command()
async def undeafen(ctx, user: discord.Member):
    """
    Command to undeafen a user in the voice channel.

    Parameters:
        - ctx (commands.Context): The context of the command.
        - user (discord.Member): The member to be undeafened.

    Usage: !undeafen <user_mention>
    """
    await user.edit(deafen=False)
    await ctx.send(f"{user.display_name} has been undeafened in the voice channel.")

@bot.command()
async def voicekick(ctx, user: discord.Member):
    """
    Command to kick a user from the voice channel.

    Parameters:
        - ctx (commands.Context): The context of the command.
        - user (discord.Member): The member to be kicked from the voice channel.

    Usage: !voicekick <user_mention>
    """
    await user.edit(voice_channel=None)
    await ctx.send(f"{user.display_name} has been kicked from the voice channel.")








































bot.run("MTE4NzYyOTkwMTkyNzQzNjMzOA.GJOdwU.D-lcgjihXqGWzaiaFwGJw4QvkKgZhRd3xAQXpY")