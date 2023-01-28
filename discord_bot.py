import discord
from discord import app_commands
from discord.ext import commands


GUILD = 1017089509269188648
TOKEN = ''
#intents = discord.Intents.default()
#intents.message_content = True
intents = discord.Intents(value = 8)

client = discord.Client(intents = intents)

tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    guild = client.get_guild(GUILD)
    global tree
    print('bot ready')
    tree.copy_global_to(guild=guild)
    await tree.sync(guild=guild)


@tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@tree.command()
async def e(interaction: discord.Interaction):
    """e"""
    await interaction.response.send_message(f'e')



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








