import discord
import random
import os
from discord.ext import commands

class eightball(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("eightball.py is ready!")

    @commands.command(alias=["8ball", "magic_eightball",])
    async def eightball(ctx, *, question):
        with open("os.chdir('./responses.txt')responses.txt", "r") as f: 
            rResponses = f.readlines()
            response = random.choice(rResponses) 

        await ctx.send(response) #user waits for response


async def setup(client):
    await client.add_cog(eightball(client))
