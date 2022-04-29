from email.contentmanager import raw_data_manager
from http.client import ImproperConnectionState
import discord
from discord.ext import commands
import json
import random
import os

#intens為特殊權限管理 member要額外開
intents = discord.Intents.default()
intents.members = True
intents.presences = True

with open("../setting.json",mode="r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

#BOT指令為$
bot = commands.Bot(command_prefix='$',intents = intents)

#上線後回傳到黑窗
@bot.event
async def on_ready():
    print(">> BOT is online <<")

#bot每個cmd的載入 卸載 重新載入
@bot.command()
async def load(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        bot.load_extension(f"cmds.{extension}")
        await ctx.send(f"Loaded {extension} done")
    else:
            await ctx.send(f"你沒資格")
@bot.command()
async def unload(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        bot.unload_extension(f"cmds.{extension}")
        await ctx.send(f"Unloaded {extension} done")
    else:
            await ctx.send(f"你沒資格")
@bot.command()
async def reload(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        bot.reload_extension(f"cmds.{extension}")
        await ctx.send(f"Reloaded {extension} done")
    else:
            await ctx.send(f"你沒資格")

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

#RUNbot
if __name__ == "__main__":
    bot.run(jdata["TOKEN"])