import discord
from discord.ext import commands
import os
import asyncio
import keep_alive

client = commands.Bot(command_prefix = '!') # The bot's prefix

@client.event
async def on_ready():
    activity = discord.Game(name="!sign | #BanRjain", type=3) # Here is where you can change the status of the bot.
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("I'm alive!") # This is what it prints in the cosole when it is ready

@client.command()
async def sign(ctx):
    if ctx.author._roles.has(role id): # This is the role that is unable to sign
        return await ctx.send(":x: | You have already signed this petition")
    else:
        await ctx.reply(f"<:RJainScammer:941399190439862293> | Successfully signed the petition for the following:\n`#BanRjain`") # You can change the name of the petition here
    log_channel = await client.fetch_channel(channel id) # The channel where it logs all of votes
    await log_channel.send(f"{ctx.author.mention} has signed the petition!") # This is the message that it sends it the logchannel
    member = ctx.author # This defines the member
    await member.add_roles(discord.Object(role id)) # This is the role that it adds


keep_alive.keep_alive()
client.run(os.getenv("TOKEN")) # Make sure to add an env token