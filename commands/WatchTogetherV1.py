# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import json
import requests
import schedule
from data import db_session
from data.wt_users import WT_user


class WT_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        db_session.global_init("db/wt_users.db")

    @commands.command(name='watch')  # Команда с рандомными мемами
    async def create_WT(self, ctx, url):
        db_sess = db_session.create_session()

        author_id = ctx.message.author.id
        nickname = ctx.message.author.nick

        q = db_sess.query(WT_user.id).filter(WT_user.discord_id==author_id)
        if not db_sess.query(q.exists()).scalar():
            params = {
            'w2g_api_key': "9h4xsjcz3qgrn0arl01jrdqccdtf2a8ad6c39jh1ujiipt7jfsyqvozrpnr9o6k9",
            'share': url,
            'bg_color': '#000000',
            'bp_opacity': '50',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
            
            response = requests.post('https://w2g.tv/rooms/create.json', params=params).json()
            with open("response_WT.json", mode='w', encoding='utf-8') as file:
                json.dump(response, file, indent=3)
            
            user = WT_user()
            user.discord_id = author_id
            user.streamkey = response['streamkey']
            user.nickname = nickname
            db_sess.add(user)
            db_sess.commit()

            await ctx.channel.send(f"Ссылка на совместный просмотр \n https://w2g.tv/rooms/{response['streamkey']}")
        else:
            params = {
            'w2g_api_key': "9h4xsjcz3qgrn0arl01jrdqccdtf2a8ad6c39jh1ujiipt7jfsyqvozrpnr9o6k9",
            'Accept': 'application/json',
            'Content-Type': 'application/json',
           'add_items': [{"url": url, "title": ""}]
        }

            user = db_sess.query(WT_user).filter(WT_user.discord_id==author_id).first()
            response = requests.post(f"https://w2g.tv/rooms/{user.streamkey}/playlists/current/playlist_items/sync_update", params=params)
            await ctx.channel.send(response)
            # with open("response_WT.json", mode='w', encoding='utf-8') as file:
            #     json.dump(response, file, indent=3)
            
            await ctx.channel.send(f"Ссылка на совместный просмотр \n https://w2g.tv/rooms/{user.streamkey}")