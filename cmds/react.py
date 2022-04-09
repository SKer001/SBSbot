import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
with open("../jfile/setting.json",mode="r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

class react(Cog_Extension):

    @commands.command()
    async def 早安(self,ctx):
        await ctx.send(f"早安")

    @commands.command()
    async def 圖片(self,ctx):
        random_pic = random.choice(jdata["pic"])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

def setup(bot):
    bot.add_cog(react(bot))