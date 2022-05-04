# -*- coding: utf-8 -*-
import discord
from os.path import getsize
from discord.ext import commands
import sys
# import sqlite3
import json
import requests
import logging
from commands.meme import Meme_command

from commands.reputation import rep_eveent
from commands.reputation import Reputation_command

TOKEN = "NzU5NDY5MjY2NTQ1Mjc5MDA3.X2983w.GsN0PNRjwyGOsaWj1lO_a2-nMXU"

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


if __name__ == '__main__':
    bot = commands.Bot(command_prefix='!')
    bot.add_cog(Meme_command(bot))
    bot.add_cog(Reputation_command(bot))
    bot.add_cog(rep_eveent(bot))
    bot.run(TOKEN)