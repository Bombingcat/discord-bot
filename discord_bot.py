import discord
import messages
import logging
import time
import random
import requests
import user_message_log
import discord.utils
from configuration import get_token
from discord import app_commands
from discord.ext import commands


GUILD = 1017089509269188648
TOKEN = get_token()
intents = discord.Intents(8)
intents.messages = True
intents.members = True
client = discord.Client(intents = intents)
tree = app_commands.CommandTree(client)


creeper_list = ['awwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww man','AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAw man','awwwwww man','awwwwwwwwwwwwwwwWWWWWWWWwwwwwwwwwwwwwwwwwwwwwwww man','awwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww man','awoewoe man','*EXPLOSION (you where too late)*','ey im walkin here','CCCCHHHHHHH','CREEPER GET THE FUCK OUT','CwEEpEw oh no','not my family please they have done nothing wrong *EXPLOSION*  NOOOOOOOOOOOOOOOOOOOOOOOOOO',
'''Creeper?
Aww, man
So we back in the mine
Got our pickaxe swinging from side to side
Side-side to side
This task, a grueling one
Hope to find some diamonds tonight, night, night
Diamonds tonight
Heads up
You hear a sound, turn around and look up
Total shock fills your body
Oh, no, it's you again
I can never forget those eyes, eyes, eyes
Eyes-eye-eyes
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
'Cause, baby, tonight
You grab your pick, shovel, and bolt again
And run, run until it's done, done
Until the sun comes up in the morning
'Cause, baby, tonight
The creeper's tryna steal all our stuff again
Just when you think you're safe
Overhear some hissing from right behind
Right-right behind
That's a nice life you have
Shame it's gotta end at this time, time, time
Time-time-time-time
Blows up''']
pp_list = ['=','==','===','====','=====','======','=======','========','=========','==========','===========','============','=============','==============','===============','================','=================','==================','===================','====================',]
spegetti = ['spagetti.jpg','spegeti.jpg','spegeti2.jpg','spegeti3.jpg','spegeti4.jpg','spegeti5.jpg','spegettmonster.jpg']

@client.event
async def on_ready():
    guild = client.get_guild(GUILD)
    user_message_log.load()
    global tree
    print('''----------------------------------
      ! FIEN BOT IS ACTIVE !''')
    tree.copy_global_to(guild=guild)
    await tree.sync(guild=guild)

@client.event
async def on_message(message):
    author = message.author
    user_message_log.inc_user_msg(author.id)
    print(author)
    # if not messages.exists(author):
    #     messages.add(author)
    # else:
    #     messages.update(author)
    # if message.author == client.user:
    #     return
    # messages.report()

@tree.command()
async def msg_counter(interaction: discord.Interaction):
    """tells you what user send how much messages"""
    await interaction.response.send_message(repr(user_message_log.message_counts))

@tree.command()
async def id_to_user(interaction: discord.Interaction):
    """decodes user id's"""
    await interaction.response.send_message('https://discord.id/')

@tree.command()
async def msg_decoder(interaction: discord.Interaction):
    """decodes user id's"""

    await interaction.response.send_message()

@tree.command()
async def test(interaction: discord.Interaction):
    """test"""
    guild = client.get_guild(GUILD)
    await interaction.response.send_message(list(guild.members))

@tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@tree.command()
async def e(interaction: discord.Interaction):
    """e"""
    await interaction.response.send_message(f'e')

@tree.command()
async def kys(interaction: discord.Interaction):
    """why does this exist again?"""
    await interaction.response.send_message(f'keep yourself safe {interaction.user.mention}')

@tree.command()
async def spegeti(interaction: discord.Interaction):
    """spegeti good"""
    await interaction.response.send_message(file = discord.File(random.choice(spegetti)))

@tree.command()
async def current_time(interaction: discord.Interaction):
    """tells you the time"""
    current_time = time.ctime()
    await interaction.response.send_message(str(current_time))

@tree.command()
async def creeper(interaction: discord.Interaction):
    """awwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww man"""
    await interaction.response.send_message((random.choice(creeper_list)))

@tree.command()
async def ppsize(interaction: discord.Interaction):
    """8=D"""
    random_pp_list = random.choice(pp_list)
    await interaction.response.send_message(str(interaction.user) + ' zijn pp: 8' + ((random_pp_list)) + ('D'))





client.run(TOKEN )







