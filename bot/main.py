import os
import discord

from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json
import random
import re
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!') #Prefix to invoke bot


@bot.event
async def on_message(message):
    # if message.author == bot.user:
    #     return


    if re.sub(r'[^\w]', '', message.content.lower()) == 'hellothere':
        response = f'{message.author.name}, Welcome back!'
        await message.channel.send(response)
    
    await bot.process_commands(message)

@bot.command(
    help="use this command to add two numbers",
    brief="Print result back to the channel.",
    name='sum')
async def sum(ctx, num1, num2):
    response = int(num1) + int(num2)
    return await ctx.send(response)


@bot.command(
    help="Use command to play vs the bot in RPS game.",
    brief="Print who is the winner back to the channel.",
    name='play')
async def play(ctx, value=""):
    RPS = ["ROCK","PAPER","SCISSORS"]
    cp_action = random.choice(RPS)
    
    if value is None or value == "":
        return   await ctx.send("I can't play if you don't put one of these values  ['ROCK', 'PAPER', 'SCISSORS'] ")
    
    value = value.upper()

    if value not in RPS:
       return   await ctx.send(f"{value} is not valid, try one of these ['ROCK','PAPER','SCISSORS']!")
         
    # await ctx.send(f"I choose {cp_action}!")
    if value == cp_action:
        await ctx.send(f"Both players selected {value}. It's a tie!")
    elif value == "ROCK":
        if cp_action == "SCISSORS":
            await ctx.send("Rock smashes scissors! You win!")
        else:
            await ctx.send("Paper covers rock! You lose.")
    elif value == "PAPER":
        if cp_action == "ROCK":
            await ctx.send("Paper covers rock! You win!")
        else:
            await ctx.send("Scissors cuts paper! You lose.")
    elif value == "SCISSORS":
        if cp_action == "PAPER":
            await ctx.send("Scissors cuts paper! You win!")
        else:
            await ctx.send("Rock smashes scissors! You lose.")
        
@bot.command(
    help="Use command to search info about character of Rick and Morty tvs show. [rick, jerry, morty, ...]",
    brief="Print info character.",
    name='search') 
async def search(ctx,name=""):
    
    
    if name is None or name == "":
        return   await ctx.send("I can't search if you don't put some value")
    
    data = urllib.request.urlopen("https://rickandmortyapi.com/api/character/?name" + name ).read()
    response = ""


    name = json.loads(data)["results"][0]["name"]
    status = json.loads(data)["results"][0]["status"]
    gender = json.loads(data)["results"][0]["gender"]
    location = json.loads(data)["results"][0]["location"]["name"]
    response = ">> " + name + " status: " + status +", gender: "+ gender + ", location: " + location
    await ctx.send(response)

@bot.command(
	help="Looks like you need some help.",
	brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)
bot.run(TOKEN)