import discord
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime


class MyCog(commands.Cog):
    """
    A custom Discord cog (extension) named MyCog.

    This cog defines a listener for the "on_message" event, a simple command "black",
    and introduces a task "alarm" with a command "startalarm" to set an alarm.

    Attributes:
    - bot (commands.Bot): The bot instance associated with this cog.

    Methods:
    - __init__(self, bot): Initializes the MyCog instance.
    - on_message(self, msg): A listener method triggered on each received message.
    - black(self, ctx): A command method responding with "White!" when invoked.
    - alarm(self, ctx, hour, minute): A task method to send a reminder when the specified time is reached.
    - startalarm(self, ctx, date): A command method to start the alarm task with a specified time.

    """
    def __init__(self, bot):
        """
        Initializes the MyCog instance.

        Parameters:
        - bot (commands.Bot): The bot instance associated with this cog.

        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        """
        A listener method triggered when a message is received.

        Parameters:
        - msg (discord.Message): The message object received.

        """
        if msg.content == "hello":
            await msg.channel.send("hey there!")

    @commands.command()
    async def black(self, ctx):
        """
        A command method responding with "White!" when invoked.

        Parameters:
        - ctx (commands.Context): The context object representing the command invocation.

        """
        await ctx.send("White!")

    @tasks.loop(seconds=1)
    async def alarm(self, ctx, hour, minute):
        """
        A task method to send a reminder when the specified time is reached.

        Parameters:
        - ctx (commands.Context): The context object representing the command invocation.
        - hour (int): The hour of the reminder time.
        - minute (int): The minute of the reminder time.

        """
        now = datetime.now().time()
        if now.hour == hour and now.minute == minute:
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send("It's time now!")
            self.alarm.stop()

    @commands.command()
    async def startalarm(self, ctx, date):
        """
        A command method to start the alarm task with a specified time.

        Parameters:
        - ctx (commands.Context): The context object representing the command invocation.
        - date (str): The time in the format "hour:minute" to set the alarm.

        Usage: !startalarm <XX:XX>

        """
        hour, minute = date.split(":")
        hour = int(hour)
        minute = int(minute)
        self.alarm.start(ctx, hour, minute)


# The setup function is typically used to add the cog to the bot.
# It is called when the cog is loaded using bot.load_extension('cog_name').
# Make sure to handle exceptions if there is an issue adding the cog.
async def setup(bot):
    """
    Sets up and adds the MyCog to the bot.

    Parameters:
    - bot (commands.Bot): The bot instance.

    """
    try:
        await bot.add_cog(MyCog(bot))
    except Exception as e:
        print(f'Error adding MyCog: {e}')
