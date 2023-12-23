import discord

intents = discord.Intents.all()
intents.message_content = True
"""
Discord introduced intents as a way to give bot developers more control over the data their bots receive from Discord servers. 
Intents are a mechanism to specify which events your bot is interested in and allowed to receive. 
This helps Discord manage and scale the amount of data sent to bots, especially in larger servers, 
and it provides more privacy and control over sensitive information.
By specifying the intents your bot needs, you reduce the amount of data sent over the WebSocket connection, making your bot more resource-efficient.
Intents help protect user privacy by restricting access to certain information, such as member lists and presence data, unless explicitly requested.
In large servers, restricting the data sent to bots based on their declared intents helps Discord manage the scalability of their systems.
"""
bot = discord.Client(intents = intents)


# this is a decorator used to modify a function, here it modifies async def on_ready() function. 
# It basically tells a discord bot that this is an event and when "on_ready" event happens, I want you to do the "print". 
# @bot.event is there to register on_ready as an actual discord event.
@bot.event #^^^
async def on_ready():
	"""
	In Python, async is a keyword used to define asynchronous functions. 
	Asynchronous programming allows you to write code that can perform non-blocking operations, 
	which is particularly useful in scenarios where you want to avoid waiting for one task to finish before starting another.
	"""
	print("DUMMY IS HERE, HOES!")

@bot.event
async def on_message(message):
	"""
	This event is called when a new text "message" is written in a discord server.
	"""
	username = message.author.display_name # This gives us the "Discord display name" of the user that sent the "message".

	if message.author == bot.user:
		"""
		We do this so that the bot does not mistake its own message for an event.
		"""
		return
	else:
		if message.content == "hello": 
			await message.channel.send("hello " + username)
			"""
			In Python, await is used in conjunction with an asynchronous function call to 
			indicate that the execution of the code should pause and wait for the asynchronous operation to 
			complete before moving on to the next line of code. 
			It is specifically used within functions defined with the async keyword.

			In simpler terms, await is a keyword used in asynchronous programming in Python. 
			When you see await, it means the program is pausing briefly to let some task finish before moving on. 
			In this code, await message.channel.send("hello") is waiting for the bot to send the message "hello" to 
			the same channel before doing anything else. It keeps the program responsive while 
			waiting for potentially slow operations, like sending a message over the internet.
			"""

@bot.event
async def on_member_join(member):
	"""
	This event triggers when someone (member) joins our discord server
	"""
	username = member.display_name
	guild = member.guild # guild is a server
	guildName = guild.name
	dmChannel = await member.create_dm() # since create_dm is a builtin discord function, we have to use await.
	await dmChannel.send(f"Hello {username}! Welcome to {guildName}.")

@bot.event
async def on_raw_reaction_add(payload):
	"""
	Called when a message has a reaction added.
	The payload in the on_raw_reaction_add event refers to the raw 
	event data related to a reaction being added to a message. 
	For example, the user id of the user that added the reaction
	"""
	emoji = payload.emoji.name
	member = payload.member 
	message_id = payload.message_id
	guild_id = payload.guild_id
	guild = bot.get_guild(guild_id)

	if emoji == "🔴" and message_id == 1188069102271598592: # Checking if a reaction with a specific emoji is added to a specific message with ID xxxxxxxxxxxxxxxxx.
		role = discord.utils.get(guild.roles, name = "The Weeknd") # Discord role object corresponding to the role named "The Weeknd" in the server (guild) where the reaction event occurred.
		await member.add_roles(role)
	if emoji == "🔵" and message_id == 1188069124295901215:
		role = discord.utils.get(guild.roles, name = "Post Malone")
		await member.add_roles(role)
	if emoji == "🟡" and message_id == 1188069134643253328:
		role = discord.utils.get(guild.roles, name = "Joji")
		await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
	"""
	Called when a message has a reaction removed.
	"""
	user_id = payload.user_id
	emoji = payload.emoji.name
	# member = payload.member # We cannot use payload.member since it is only available if event_type is REACTION_ADD.
	message_id = payload.message_id
	guild_id = payload.guild_id
	guild = bot.get_guild(guild_id)
	member = guild.get_member(user_id) # Alternate way to get the payload member. Since we can get the user id from the payload event, we can use that to get the member from the guild.

	if emoji == "🔴" and message_id == 1188069102271598592:
		role = discord.utils.get(guild.roles, name = "The Weeknd")
		await member.remove_roles(role)
	if emoji == "🔵" and message_id == 1188069124295901215:
		role = discord.utils.get(guild.roles, name = "Post Malone")
		await member.remove_roles(role)
	if emoji == "🟡" and message_id == 1188069134643253328:
		role = discord.utils.get(guild.roles, name = "Joji")
		await member.remove_roles(role)


bot.run("MTE4NzYyOTkwMTkyNzQzNjMzOA.GJOdwU.D-lcgjihXqGWzaiaFwGJw4QvkKgZhRd3xAQXpY")