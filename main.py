import discord
from discord.ext import commands
# import sqlite3
import json
import requests

TOKEN = "OTUxOTg5Nzg1OTk0NjEyNzQ3.YivflA.I-_BXijOvOLraOcN9qsxUyYbbqQ"


class Bot_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='meme')
    async def meme(self, ctx):
        URL = "https://api.humorapi.com/memes/random"
        params = {
            'api-key': "59bf2775d7c244aeac828e67f4f05ca0"
        }
        response = requests.get(URL, params).json()
        await ctx.channel.send(response['url'])


bot = commands.Bot(command_prefix='!')
bot.add_cog(Bot_commands(bot))
bot.run(TOKEN)