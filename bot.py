from sys import intern
import discord
from discord.ext import commands
#intens為特殊權限管理 member要額外開
intens = discord.Intents.default()
intens.members = True


#BOT指令為$
bot = commands.Bot(command_prefix='$',intens = intens)
#上線後回傳到黑窗
@bot.event
async def on_ready():
    print(">> BOT is online <<")

#diediediediediediediediediediediediediediediediediedie
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(921239567611351093)
    await channel.send(f"{member} join!")
    print(f"{member} join!")                             #joun and leave 壞死

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(921239567611351093)
    await channel.send(f"{member} join!")
    print(f"{member} leave!")
#diediediediediediediediediediediediediediediediediedie

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} (ms)")

@bot.command()
async def number5(ctx):
    await ctx.send(f"別玩手機")

@bot.command()
async def 早安(ctx):
    await ctx.send(f"早安")

#RUNbot
bot.run("OTU2MjEwOTE5NDc2Njk1MDYw.Yjs60A.nLYRWIUG3_INe-do5QweWZLAYvI")