from discord.ext import commands
from commands import misc,geography
import os

bot = commands.Bot(
    command_prefix='$'
)

bot.add_cog(misc.Misc(bot))

bot.add_cog(geography.Geography(bot, 'src/datas/capitales.csv', 'src/datas/drapeaux.csv'))

bot.run(os.getenv("DISCORD_TOKEN"))
