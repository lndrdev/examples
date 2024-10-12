from discord.ext import commands
from discord.commands import slash_command
import ezcord

class Cog(ezcord.Cog):

    @slash_command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong!")

def setup(bot: ezcord.Bot):
    bot.add_cog(Cog(bot))
