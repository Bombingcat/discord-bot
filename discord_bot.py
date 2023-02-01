import discord
import messages
import logging
import time
from configuration import get_token
from discord import app_commands
from discord.ext import commands


GUILD = 1017089509269188648
TOKEN = get_token()
#intents = discord.Intents.default()
#intents.message_content = True
intents = discord.Intents(value = 8)

client = discord.Client(intents = intents)

tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    guild = client.get_guild(GUILD)
    global tree
    print('''----------------------------------
        ! FIEN BOT IS ACTIVE !''')
    tree.copy_global_to(guild=guild)
    await tree.sync(guild=guild)

@client.event
async def on_message(message):
    author = message.author
    if not messages.exists(author):
        messages.add(author)
    else:
        messages.update(author)
    if message.author == client.user:
        return
    messages.report()


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
async def time(interaction: discord.Interaction):
    """tells you the exact time"""
    current_time = time.ctime()
    await interaction.response.send_message((current_time))







# @client.event
# async def on_message(message):
#     channel = client.get_channel(1030698526075785298)
#     await channel.send('testing')
#     print(message.author, message.content, message.channel.id)
#     pass


# @client.command()
# async def hello(ctx):
#     channel = client.get_channel(1033759192596619386)
#     await channel.send(f'hello there {ctx.author.mention}')

client.run(TOKEN)








