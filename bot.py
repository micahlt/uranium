import discord
from discord.ext import commands
prefix = "u!"
bot = commands.Bot(command_prefix='u!')
await client.change_status(game=discord.Game(name='ah, I see now'))

@bot.event
async def on_ready():
    print("ready")
@bot.event
async def on_message(message):
    print("CONTENT:", message.content)

@bot.command()
async def ping(ctx):
    '''
    THIS STEAM
    '''
    
    latency = bot.latency
    await ctx.send(latency)
    
