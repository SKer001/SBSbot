import discord
from discord.ext import commands
#BOT指令為$
bot = commands.Bot(command_prefix='$')
#上線後回傳到黑窗
@bot.event
async def on_ready():
    print(">> BOT is online <<")
#RUNbot
bot.run("OTU2MjEwOTE5NDc2Njk1MDYw.Yjs60A.pFWDyR_aj6QoOzATS5hNUvBYyTs")