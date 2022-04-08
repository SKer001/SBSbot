import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
with open("setting.json",mode="r",encoding="utf8") as jfile:
    jdata = json.load(jfile)
    
class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata["Welcome_Channel"]))
        await channel.send(f"@everyone {member} join!")
        print(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata["Leave_Channel"]))
        await channel.send(f"@everyone {member} leave!")
        print(f"{member} leave!")

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith("崧瀚"):
            await msg.channel.send(f"教官來了")

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith("早安"):
            await msg.channel.send(f"早ㄤ阿")

def setup(bot):
    bot.add_cog(event(bot))