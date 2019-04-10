import discord
from discord.ext import commands
prefix = "u!"
bot = commands.Bot(command_prefix='u!')
await client.change_status(game=discord.Game(name='ah, I see now'))
bot.run('NTY1NTAzNjk2ODE4MTQzMjUz.XK3ZkA.qBfm0al8bXW-3T7r0GJ2n8DvdhA')
@bot.event
async def on_ready():
    print("ready")
async def on_message(message):
    print("CONTENT:", message.content)

@bot.command()
async def ping(ctx):
    '''
    THIS STEAM
    '''
    
    latency = bot.latency
    await ctx.send(latency)
    
