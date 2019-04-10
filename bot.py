import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='u!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await client.change_status(game=discord.Game(name='whatever'))

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")
    await

bot.run('NTY1NTAzNjk2ODE4MTQzMjUz.XK3ZkA.qBfm0al8bXW-3T7r0GJ2n8DvdhA')
