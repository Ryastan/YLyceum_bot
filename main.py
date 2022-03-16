import discord
from discord.ext import commands
# import sqlite3
import json
import requests

TOKEN = ""


class Bot_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='meme') #Команда с рандомными мемами
    async def meme(self, ctx):
        URL = "https://api.humorapi.com/memes/random" #URL randomMeMe
        params = {
            'api-key': "59bf2775d7c244aeac828e67f4f05ca0"
        }
        response = requests.get(URL, params).json()
        await ctx.channel.send(response['url']) #Вывод ссылки(картинки) с мемом


bot = commands.Bot(command_prefix='!')
bot.add_cog(Bot_commands(bot))
bot.run(TOKEN)