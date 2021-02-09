from discord.ext import commands
from commands import misc,capitals
import os

bot = commands.Bot(
    command_prefix='$'
)

bot.add_cog(misc.Misc(bot))
bot.add_cog(capitals.Capitals.LoadFromCSV(bot, 'src/datas/capitales.csv'))

bot.run(os.getenv("DISCORD_TOKEN"))
