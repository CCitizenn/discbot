import discord
import ssl
import random
import asyncio
import os
from discord.ext import commands , tasks
from itertools import cycle

ssl._create_default_https_context = ssl._create_unverified_context 
client = commands.Bot(command_prefix="!", intents=discord.Intents.all()) #sets prefix of bot to !

#async functions must have an await and vice versa.


async def main():
    async with client:
        await load()
        await client.start("MTE1OTU2MjEzMTA4NDE2MTAyNA.GuURkg.s7c7vYLroG21w_g2pzFF-cgd__HP9ck8pHmRxQ")

bot_status = cycle(["Mice Catching Simulator!", "Meow", "How to take over the world: for Dummies", "Pussy Simulator 3", "Wildlife video of Birds"])
@tasks.loop(seconds=7) # changes every 3 seconds
async def change_status():
    await client.change_presence(activity = discord.Game(next(bot_status))) #discord.Game is saying it will display as if its playing a game


@client.event
async def on_ready():
    print(f"Success: Kitty-3000 is connected to Discord")
    change_status.start()

#@client.command(alias=["8ball", "magic_eightball", ""])
#async def eightball(ctx, *, question):
#    with open("responses.txt", "r") as f: #open file in read mode with alias "f"
#        rResponses = f.readlines()
#        response = random.choice(rResponses) 
#
#    await ctx.send(response) #user waits for response

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}") # would say its loaded "cog" and not "cog.py" by splicing file name
            print(f"{filename[:-3]} is loaded!")



asyncio.run(main())