import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents=intents)

@bot.command()
async def join(ctx):
	channel = ctx.author.voice.channel
	await channel.connect()

























bot.run("MTE4NzYyOTkwMTkyNzQzNjMzOA.Gir1Ze.uuLFBYszePLmFRK5tHNvXYypGr1l6kAsqDKguo")



