import discord
from discord.ext import commands
import json
import requests
import schedule


class Meme_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='meme')  # Команда с рандомными мемами
    async def meme(self, ctx):
        URL = "https://api.humorapi.com/memes/random"  # URL randomMeMe
        params = {
            'api-key': "59bf2775d7c244aeac828e67f4f05ca0"
        }
        response = requests.get(URL, params).json()
        with open('response.json', mode='w', encoding='utf-8') as file:
            json.dump(response, file)
        try:
            await ctx.channel.send(response['url'])  # Вывод ссылки(картинки) с мемом
        except KeyError:
            if response['status'] == 'failure' and response['code'] == 402:
                await ctx.channel.send('Ошибка(\nМемы на сегодня закончились')
            else:
                await ctx.channel.send(f"Ошибка {response['code']} Обратитесь к разработчиками для решения проблемы")

    @commands.command(name='meme in')  # Команда для установки времени для мема
    async def time_meme(self, ctx):
        pass
