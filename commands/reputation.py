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
        with open('reputation.json') as rep_file:
            data = json.load(rep_file)
        if str(ctx.author.bot) in rep_file:
            rep_file[str(ctx.author.bot)] += 1
        else:
            rep_file[str(ctx.author.bot)] = 1
        await ctx.channel.send("Ваша репутация теперь равна", str(rep_file[str(ctx.author.bot)]))
        with open('reputation.json', 'w') as cat_file:
            json.dump(rep_file, cat_file)