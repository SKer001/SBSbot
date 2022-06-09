import imp
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
import asyncio

with open("cmds/Pokemos.json",mode="r",encoding="utf-8") as file:
    Gfile = json.load(file)

class game(Cog_Extension):

    @commands.group()
    async def game(self,ctx):
        pass

    @game.command()
    async def Pokemo_GO(self,ctx,ball):
        person = str(ctx.author.name)
        if ball == "精靈球":
            catched = random.choice(Gfile["normal"])
            await ctx.send("抓捕中.....")
            await asyncio.sleep(3)
            msg = "成功! " + person + "抓到了" + catched
            await ctx.send(msg)
            

        
        




def setup(bot):
    bot.add_cog(game(bot))