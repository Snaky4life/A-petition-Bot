import discord
from discord.ext import commands
import os
import asyncio
import keep_alive

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    activity = discord.Game(name="!sign", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("I'm alive!")

@client.command()
async def sign(ctx):
    ty = await ctx.reply(":white_check_mark: | Successfully signed the petition for the following:\n`#BanRjain`")
    await asyncio.sleep(5)
    await ty.delete()
    channel = await client.fetch_channel(940779168193445959)
    await channel.send(f"{ctx.author.mention} has signed the petition!")

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))