import discord
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='v', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {bot.latency * 1000:.2f} ms')

@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

@bot.event
async def on_message(message):
    if message.channel.id == 954711669496512512:
      if message.attachments:
        for attachment in message.attachments:
                channel = bot.get_channel(954711698957291531)
                await channel.send(attachment.url)
        await bot.process_commands(message)
token = ./
bot.run(token)
