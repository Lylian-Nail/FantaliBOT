import asyncio
import random
import csv
from discord.ext import commands

class Capitals(commands.Cog):

    def __init__(self, bot, capitals):
        self.bot = bot
        self.capitals = capitals

    @classmethod
    def LoadFromCSV(cls, bot, csv_file):
        with open(csv_file, 'r', newline='') as csvfd:
            rows = csv.reader(csvfd, delimiter=';')

            capitals = {}
            for row in rows:
                capitals[row[0].capitalize()] = [entry.capitalize() for entry in row[1:]]
            return Capitals(bot, capitals)

    @commands.command(
        name='capitale',
        description='Devine la capitale d\'un pays, réponds avec le bon nom de capitale dans le message suivant',
        brief='Essaye de deviner la capitale du pays indiqué!'
    )
    async def _guess_capital(self, ctx):
        rand_country = random.choice(list(self.capitals.keys()))
        await ctx.channel.send(f'Devine la capitale de {rand_country}!')

        msg = None
        try:
            msg = await self._wait_response(ctx.author, ctx.channel, timeout=10)
        except asyncio.TimeoutError:
            await ctx.channel.send(f'Tu n\'as que 10 secondes pour répondre! Dommage')
            return
        
        answer = self._check_answer(msg.content, self.capitals[rand_country])
        if answer != False:
            await ctx.channel.send(f"Bien joué tu as deviné {answer}!")
        else:
            await ctx.channel.send(f"Et nan! La capitale de {rand_country} est {self.capitals[rand_country][0]}")

    async def _wait_response(self, user, channel, timeout=None):
        msg = await self.bot.wait_for('message', timeout=timeout)
        while msg.author != user or msg.channel != channel:
            msg = await self.bot.wait_for('message', timeout=timeout)
        return msg

    def _check_answer(self, message_content, capitals):
        message_content = message_content.title()

        for capital_name in capitals:
            if capital_name in message_content:
                return capital_name
        return False
