from discord.ext import commands
from commands import misc,geography
from config.config import config

bot = commands.Bot(
    command_prefix='$'
)

# Load conf from 'config/config.ini'
config = config()

bot.add_cog(misc.Misc(bot))
bot.add_cog(geography.Geography(bot, 'src/datas/capitales.csv', 'src/datas/drapeaux.csv'))

bot.run(config['discord']['token'])
