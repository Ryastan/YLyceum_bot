import discord
from discord.ext import commands
import sys
# import sqlite3
import json
import requests
import logging
from commands.meme import Meme_command
from commands.WatchTogetherV1 import WT_command

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = ""


if __name__ == '__main__':

    bot = commands.Bot(command_prefix='!')
    bot.add_cog(Meme_command(bot))
    bot.add_cog(WT_command(bot))
    bot.run(TOKEN)