import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #events must use this instead of @client.event()
    async def on_ready(self):
        print("ping.py is ready!")

    @commands.command() # in cogs events must use commands.command() not @client.command()
    async def ping(self,ctx): # must put self before putting ANY paramaters within a class
        bot_latency = round(self.client.latency * 1000) 
        await ctx.send(f"pong! {bot_latency}ms") 
 

async def setup(client):
    await client.add_cog(Ping(client))
