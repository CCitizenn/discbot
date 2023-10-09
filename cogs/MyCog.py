import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("MyCog.py is online")

    @commands.command()
    async def embed(self, ctx):
        embedMsg = discord.Embed(title="Test", description="description of embed", color = discord.color.Green() )
        embedMsg.set_author(name=f"requested by {ctx.author.mention}", icon_url = ctx.author.avatar)
        embedMsg.set_thumbnail(url=ctx.guild.icon)
        embedMsg.image(url=ctx.guild.icon)
        embedMsg.add_field(name="field name", value="field value", inline=False) #inline=true makes everything left to right, false is top to bottom
        embedMsg.set_footer(text="this is the footer", icon_url= None)

        await ctx.send(embed = embedMsg)

async def setup(client):
    await client.add_cog(MyCog(client))

