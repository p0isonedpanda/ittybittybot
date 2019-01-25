import discord
import json
from discord.ext import commands
import random

with open('config.json') as json_file:
    config = json.load(json_file)

bot = commands.Bot(command_prefix=config['prefix'], description='')

@bot.event
async def on_ready():
    print('Logged in: ' + bot.user.name)

@bot.command()
async def ping():
    """checks if we're still up and running"""
    await bot.say('i\'m still alive, don\'t worry!')

bot.run(config['token'])
