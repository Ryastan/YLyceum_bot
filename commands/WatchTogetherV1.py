import discord
from discord.ext import commands
import json
import requests
import schedule
from DataBase import db_session

class WT_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        db_session.global_init("db/wt_users.db")
    
    @commands.command(name='watch') #Команда с рандомными мемами
    async def create_WT(self, ctx, url):
        self.params = {
            'w2g_api_key': "9h4xsjcz3qgrn0arl01jrdqccdtf2a8ad6c39jh1ujiipt7jfsyqvozrpnr9o6k9",
            'share': url,
            'bg_color': '#000000',
            'bp_opacity': '50',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.post('https://w2g.tv/rooms/create.json', params=self.params).json()
        with open("response_WT.json", mode='w', encoding='utf-8') as file:
            json.dump(response, file, indent=3)
        
        await ctx.channel.send(f"Ссылка на совместный просмотр \n https://w2g.tv/rooms/{response['streamkey']}")
    
    @commands.command(name='add_video')
    async def add_video_WT(self, ctx, url):
        response = requests.post('https://w2g.tv/rooms/{streamkey}/playlists/current/playlist_items/sync_update', params=self.params).json()
        with open("response_WT.json", mode='w', encoding='utf-8') as file:
            json.dump(response, file, indent=3)
        
        if True:
            await ctx.channel.send(f'Видео успешно добавлено в плейлист \n Ссылка на совместный просмотр плейлиста')
        else:
            await ctx.channel.send(f'Произошло ошибка, обратитесь к разработчками для решения проблемы')
