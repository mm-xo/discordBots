import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents=intents)

@bot.command()
async def join(ctx):
	channel = ctx.author.voice.channel
	await channel.connect()

@bot.command()
async def leave(ctx):
	# channel = ctx.author.voice.channel
	await ctx.voice_client.disconnect()























bot.run("bot token here")



