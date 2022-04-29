import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(965177864787988560)
            while not self.bot.is_closed():
                count = 0
                while count>=0:
                    count += 1
                    await asyncio.sleep(3600)
                    await self.channel.send("已跑了"+str(count)+"小時")

        self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(965177864787988560)
            while not self.bot.is_closed():
                UTC0 = datetime.datetime.today()  # 獲得當地時間
                GMT8 = datetime.timedelta(hours=8)  # 時差
                TWTime = UTC0 + GMT8
                TWTime = TWTime.strftime("%H%M")
                with open("./setting.json",mode="r",encoding="utf8") as file:
                    jdata = json.load(file)
                if TWTime == jdata["loop_time"]:
                    await self.channel.send("@everyone 早安ㄤ")
                    await asyncio.sleep(60)
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())


    @commands.command()
    async def set_channel(self,ctx, chid:int):
        if  ctx.message.author.id == 403895664666214400:
            self.channel = self.bot.get_channel(chid)
            await ctx.send(f"set channel: {self.channel.mention}")
        else:
            await ctx.send(f"你沒資格")

    @commands.command()
    async def set_time(self,ctx,*,time):
        if  ctx.message.author.id == 403895664666214400:
            with open("../setting.json",mode="r",encoding="utf8") as file:
                jdata = json.load(file)
            jdata["loop_time"] = time
            with open("../setting.json",mode="w",encoding="utf8") as file:
                json.dump(jdata,file,indent=4)
            await ctx.send(f"set time: "+time)
        else:
            await ctx.send(f"你沒資格")

def setup(bot):
    bot.add_cog(task(bot))