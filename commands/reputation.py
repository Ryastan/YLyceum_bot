from os.path import getsize

import discord
import json
from discord.ext import commands
import json
import requests
import schedule


class Reputation_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='myrep')  # Команда с репутацие пользоваеля
    async def meme(self, ctx):
        try:
            f = open('reputation.txt', 'r')
        except FileNotFoundError:
            f = open('reputation.txt', 'w')
            f.close()
            f = open("reputation.txt", "r")
        data = f.read()
        data = data.split("\n")
        if getsize("reputation.txt"):
            for i in range(len(data)):
                if data[i] != "":
                    data[i] = {str(data[i].split(":")[0]): int(data[i].split(":")[1])}
        else:
            data = []
        f.close()
        ins = -1
        for i in range(len(data)):
            if str(ctx.message.author) in data[i]:
                ins = i
        if ins >= 0:
            data[ins][str(ctx.message.author)] += 1
            print(12312312313)
        else:
            data.append({str(ctx.message.author): 1})
        f = open('reputation.txt', 'w')
        for i in range(len(data)):
            for key in data[i]:
                f.write(str(key + ":" + str(data[i][key]) + "\n"))
        say = "Ваша рпутация:" + str(data[ins][key])
        await ctx.channel.send(say)
        f.close()
        print(1)