import discord
from discord.ext import commands
import requests
import schedule

class WT_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='watch') #Команда с рандомными мемами
    async def create_WT(self, ctx, url):
        params = {
            'w2g_api_key': "9h4xsjcz3qgrn0arl01jrdqccdtf2a8ad6c39jh1ujiipt7jfsyqvozrpnr9o6k9",
            'share': url,
            'bg_color': '#00ff00',
            'bp_opacity': '50'
        }
        response = requests.get('https://w2g.tv/rooms/create.json')
        print(response)