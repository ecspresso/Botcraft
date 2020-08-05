import discord
from discord.ext import commands

class Heroes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['h'])
    async def heros(self, ctx, *args):
        message = """Heroes:
        S-rank: ???
        A-rank: !!!"""

        await ctx.send(message)


def setup(bot):
    bot.add_cog(Heroes(bot))