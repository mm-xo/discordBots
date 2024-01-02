from discord.ext import commands

import discord
from discord.ext import commands

class MyCog(commands.Cog):
    """
    A custom Discord cog (extension) named MyCog.

    This cog defines a listener for the "on_message" event and a simple command "black".

    Attributes:
    - bot (commands.Bot): The bot instance associated with this cog.

    Methods:
    - __init__(self, bot): Initializes the MyCog instance.
    - on_message(self, msg): A listener method triggered on each received message.
    - black(self, ctx): A command method responding with "White!" when invoked.

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
