import discord
from discord.ext import commands
import sys
# import sqlite3
import json
import requests

sys.path.insert(1, '/commands')
from meme import Bot_commands

TOKEN = ""


if __name__ == '__main__':
    bot = commands.Bot(command_prefix='!')
    bot.add_cog(Bot_commands(bot))
    bot.run(TOKEN)