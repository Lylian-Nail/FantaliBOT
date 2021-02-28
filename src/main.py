from discord.ext import commands
from commands import misc,geography
from scores.scores import Scores
from config.config import config
import mariadb
import sys

bot = commands.Bot(
    command_prefix='$'
)

# Load conf from 'config/config.ini'
config = config()

# Connect to db
database = config['database']
try:
    conn = mariadb.connect(
        user=database['user'],
        password=database['password'],
        database=database['database'],
        host=database['host'],
        port=int(database['port'])
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
conn.autocommit = True

scores = Scores(conn.cursor(), database['database'])

bot.add_cog(misc.Misc(bot))
bot.add_cog(geography.Geography(
    bot,
    scores,
    'src/datas/capitales.csv',
    'src/datas/drapeaux.csv')
)

bot.run(config['discord']['token'])
