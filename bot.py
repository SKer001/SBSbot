import discord
from discord.ext import commands
#BOT指令為$
bot = commands.Bot(command_prefix='$')
#上線後回傳到黑窗
@bot.event
async def on_ready():
    print(">> BOT is online <<")
#RUNbot
bot.run("OTU2MjEwOTE5NDc2Njk1MDYw.Yjs60A.rC0ioNJICJ0AyATWBgXW1GO288U")

@bot.event
async def on_member_join(member):
    print(f"[member] join!")

@bot.event
async def on_member_remove(member):
    print(f"[member] leave!")