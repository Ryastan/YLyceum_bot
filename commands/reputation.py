import discord
from discord.ext import commands
import json
import requests
import schedule


class Reputation_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='myrep')  # Команда с репутацие пользоваеля
    async def meme(self, ctx):
        await ctx.channel.send("Пытаюсь сделать работу с базой в txt файле")