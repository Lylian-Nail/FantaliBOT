from discord.ext import commands
from commands import misc,capitals

bot = commands.Bot(
    command_prefix='$'
)

bot.add_cog(misc.Misc(bot))
bot.add_cog(capitals.Capitals.LoadFromCSV(bot, 'src/datas/capitales.csv'))

bot.run('ODA4NzI2NDk1MzI1NDU0Mzc2.YCKvPQ.Nv_yVSMuf4eyJR0heGlbAm-cGpw')
