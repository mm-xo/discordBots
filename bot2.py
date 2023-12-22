import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@tree.command(name = "greet", description = "My first application Command", guild=discord.Object(id=1175037117995417632)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction, user: discord.Member):
    await interaction.response.send_message(f"Hello! {user.display_name}")

@tree.command(name = "bakaaa", description = "My first application Command", guild=discord.Object(id=1175037117995417632))
async def baka(ctx, user: discord.Member):
    username = user.name
    await ctx.response.send_message(f'{username} is a baka')


@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1175037117995417632))
    print("Ready!")

@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author != bot.user:
        if msg.content == "hello":
            await msg.channel.send("hello! " + username)



































bot.run("MTE3NTA1MDcyMjAxOTExOTEyNA.G36_v-.Uxa_-rERdOwehx1jMY1VQIxEE3ZOmc4XkdpH2U")