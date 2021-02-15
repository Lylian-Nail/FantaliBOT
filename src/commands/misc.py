from discord.ext import commands
from scrapper import utils
import discord
import os

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.schmout = 0

    @commands.command(
        name='hello',
        help='Respond hello to the user, mentionning him',
        brief='Say hello to the user'
    )
    async def _say_hello(self, ctx):
        await ctx.channel.send(
            f'Hello {ctx.author.mention}!'
        )

    @commands.command(
        name='face',
        help='Respond with a fake person image from https://thispersondoesnotexist.com/',
        brief='Respond with a fake face image',
    )
    async def _fake_face(self, ctx):
        utils.download_img('https://thispersondoesnotexist.com/image', name='image.png', path='./temp')
        await ctx.channel.send(file=discord.File('./temp/image.png'))
        os.remove('./temp/image.png')

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
        elif 'schmout' in message.content and self.schmout != 5:
            mymy = await self.bot.fetch_user(261886941782343680)
            if mymy is not None:
                self.schmout += 1
                await message.channel.send(
                    f'Ah tu schmouts {mymy.mention}'
                )
