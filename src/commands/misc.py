from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='hello',
        help='Respond hello to the user, mentionning him',
        brief='Say hello to the user'
    )
    async def _say_hello(self, ctx):
        await ctx.channel.send(
            f'Hello {ctx.author.mention}!'
        )

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if 'fanta' in message.content:
            await message.channel.send(
                'Ouais mais c\'est pas toi qui décide!'
            )
        elif 'quad' in message.content:
            await message.channel.send(
                'Fils de pute rends mon quad!'
            )
