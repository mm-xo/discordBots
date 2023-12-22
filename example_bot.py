import discord
from discord import app_commands
# from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

# client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='!', help_command=None,intents=intents)
@tree.command(name = "bakaaa", description = "My first application Command", guild=discord.Object(id=1175037117995417632))
async def baka(interaction, user: discord.Member):
    username = user.name
    await interaction.response.send_message(f'{username} is a baka') 

@bot.event
async def on_ready():
    print(f'We have logged in as examplebot')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'hello':
        await message.channel.send('Hello!')

    if message.content.startswith('$MM'):
        await message.channel.send('MM The Great')

# intents = discord.Intents.all()


# @bot.event
# async def on_ready():
#     print(f'{bot.user} has connected to Discord!')

# @bot.command()
# async def greet(ctx):
#     await ctx.send(f'Hello {ctx.author.name}!')

# @bot.command()
# async def say(ctx, *, message):
#     await ctx.send(message)

# @bot.command()
# async def add(ctx, a: int, b: int):
#     await ctx.send(a + b)



































bot.run('MTE3NTAzNDc3NDkwNjIwODI5Ng.GWdBCX._J6qb5iVhD-9vnPTt-0pf_4jK0vGJBkpnDWUG8')
# client.run('MTE3NTAzNDc3NDkwNjIwODI5Ng.Gw1T7N.SaN7RuMjdZkJPumtfu5qPbH5Vtdlay2G9RflOw')






