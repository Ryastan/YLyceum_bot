import discord
from discord.ext import commands, tasks
import json
import requests
import asyncio
import datetime
from itertools import cycle


class Meme_command(commands.Cog):
    def __init__(self, bot):
        self.time = 0
        self.bot = bot
        self.client = discord.Client()
        self.everydays_meme.start()

    @commands.command(name='meme')  # Команда с мемами по ключевому слову
    async def meme(self, ctx, keyword=''):
        channel_id = ctx.channel.id
        channel = self.bot.get_channel(channel_id)
        URL = "https://api.humorapi.com/memes/search"  # URL randomMeMe
        params = {
            'api-key': "59bf2775d7c244aeac828e67f4f05ca0",
            'keywords': keyword
        }
        response = requests.get(URL, params).json()
        with open('response.json', mode='w', encoding='utf-8') as file:
            json.dump(response, file, indent=3)
        try:
            await channel.send(response['url'])  # Вывод ссылки(картинки) с мемом
        except KeyError:
            if response['status'] == 'failure' and response['code'] == 402:
                await channel.send('Ошибка(\nМемы на сегодня закончились')
            else:
                await channel.send(f"Ошибка {response['code']} Обратитесь к разработчиками для решения проблемы")

    @commands.command(name='random_meme')  # Команда с рандомными мемами
    async def meme(self, ctx):
        channel_id = ctx.channel.id
        channel = self.bot.get_channel(channel_id)
        URL = "https://api.humorapi.com/memes/random"  # URL randomMeMe
        params = {
            'api-key': "59bf2775d7c244aeac828e67f4f05ca0"
        }
        response = requests.get(URL, params).json()
        with open('response.json', mode='w', encoding='utf-8') as file:
            json.dump(response, file, indent=3)
        try:
            await channel.send(response['url'])  # Вывод ссылки(картинки) с мемом
        except KeyError:
            if response['status'] == 'failure' and response['code'] == 402:
                await channel.send('Ошибка(\nМемы на сегодня закончились')
            else:
                await channel.send(f"Ошибка {response['code']} Обратитесь к разработчиками для решения проблемы")

    @commands.command(name='meme_everyday_at')  # Команда для установки времени для мема
    async def time_meme(self, ctx, time):
        self.channel_meme_id = ctx.channel.id
        self.channel = self.bot.get_channel(self.channel_meme_id)
        self.time = datetime.datetime.now()
        self.time = self.time.strftime('%H:%M')
        try:
            self.schedule_time = time.split(':')
            if len(self.schedule_time) == 1:
                raise Exception
            await ctx.channel.send(self.time)
        except Exception:
            await ctx.channel.send('Неправильный формат ввода времени')
            await ctx.channel.send('Пример: !meme_everyday_at 9:01')

    @tasks.loop(seconds=60.0)
    async def everydays_meme(self):
        if self.time == 0:
            print('not time')
        else:
            time = datetime.datetime.now()
            time = time.strftime('%H:%M')
            print(time, self.time)
            if self.time == time:
                channel = self.channel
                URL = "https://api.humorapi.com/memes/random"  # URL randomMeMe
                params = {
                    'api-key': "59bf2775d7c244aeac828e67f4f05ca0"
                }
                response = requests.get(URL, params).json()
                with open('response.json', mode='w', encoding='utf-8') as file:
                    json.dump(response, file, indent=3)
                try:
                    await channel.send(response['url'])  # Вывод ссылки(картинки) с мемом
                except KeyError:
                    if response['status'] == 'failure' and response['code'] == 402:
                        await channel.send('Ошибка(\nМемы на сегодня закончились')
                    else:
                        await channel.send(
                            f"Ошибка {response['code']} Обратитесь к разработчиками для решения проблемы")