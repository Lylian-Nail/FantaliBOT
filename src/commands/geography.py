import asyncio
import random
import flag
import csv
from discord.ext import commands

class Geography(commands.Cog):

    def __init__(self, bot, csv_capitals, csv_flags):
        self.bot = bot
        self.capitals = self.load_from_csv(csv_capitals)
        self.flags = self.load_from_csv(csv_flags)

    @commands.command(
        name='capitale',
        description='Devine la capitale d\'un pays, réponds avec le bon nom de capitale dans le message suivant',
        brief='Essaye de deviner la capitale du pays indiqué!'
    )
    async def _guess_capital(self, ctx):
        rand_country = random.choice(list(self.capitals.keys()))
        await ctx.channel.send(f'Devine la capitale de {rand_country.title()}!')

        msg = None
        try:
            msg = await self._wait_response(ctx.author, ctx.channel, timeout=10)
        except asyncio.TimeoutError:
            await ctx.channel.send(f'Tu n\'as que 10 secondes pour répondre! Dommage')
            return
        
        answer = self._check_answer(msg.content.lower(), self.capitals[rand_country])
        if answer != False:
            await ctx.channel.send(f'Bien joué tu as deviné {answer.title()}!')
        else:
            await ctx.channel.send(f'Et nan! La capitale de {rand_country.title()} est {self.capitals[rand_country][0].title()}')

    @commands.command(
        name='drapeau',
        description='Devine le drapeaux d\'un pays avec les emojis discord !',
        brief='Devine le drapeaux d\'un pays avec les emojis discord !'
    )
    async def _guess_flag(self, ctx):
        rand_country = random.choice(list(self.flags.keys()))
        await ctx.channel.send(f'Devine le drapeau de {rand_country.title()}')

        msg = None
        try:
            msg = await self._wait_response(ctx.author, ctx.channel, timeout=15)
        except asyncio.TimeoutError:
            await ctx.channel.send(f'Tu n\'as que 15 secondes pour répondre! Dommage')
            return

        flag_emoji = flag.flag(self.flags[rand_country][0])
        if flag_emoji in msg.content:
            await ctx.channel.send(f'Bien joué le drapeau de {rand_country.title()} est bien {flag_emoji}!')
        else:
            await ctx.channel.send(f'Et nan! Le drapeau de {rand_country.title()} est {flag_emoji}!')

    async def _wait_response(self, user, channel, timeout=None):
        msg = await self.bot.wait_for('message', timeout=timeout)
        while msg.author != user or msg.channel != channel:
            msg = await self.bot.wait_for('message', timeout=timeout)
        return msg

    def _check_answer(self, message_content, answers):
        for answer in answers:
            if answer in message_content:
                return capital_name
        return False

    def load_from_csv(self, csv_file):

        with open(csv_file, 'r', newline='') as csvfd:
            rows = csv.reader(csvfd, delimiter=',')

            data = {}
            for row in rows:
                data[row[0].lower()] = [entry.lower() for entry in row[1:]]
            return data