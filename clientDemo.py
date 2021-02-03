import os

import discord
from dotenv import load_dotenv
import re
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if re.sub(r'[^\w]', '', message.content.lower()) == 'hellothere':
        response = f'{message.author.name}, Welcome back!'
        await message.channel.send(response)

client.run(TOKEN)