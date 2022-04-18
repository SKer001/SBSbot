import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

    @commands.command()
    async def about(self,ctx):
        embed=discord.Embed(
        title="about bot"
        , url="https://github.com/SKer001/SBSbot"
        , description="github"
        , color=0x00ccff
        ,timestamp=datetime.datetime.utcnow()
        )
        embed.set_image(url="https://p1-tt.byteimg.com/origin/pgc-image/761f52af36d24a23a8545fcfcbf5a0fe.jpg")
        embed.set_author(
        name="幽靈夜閃"
        , url="https://github.com/SKer001"
        , icon_url="https://yt3.ggpht.com/VXeA7tz-RsePrgKKs99aYb8wz4aLSLH52lysXXpL8xH2mZt3dY65ae_0boggAy_Cy0t_3EzJ=s400-c-k-c0x00ffffff-no-rj")
        embed.set_thumbnail(url="https://i.pinimg.com/736x/e0/24/21/e02421c323d4bac3f23f429292549126.jpg")
        embed.add_field(name="作者DC", value="幽靈夜閃#3443", inline=True)
        embed.add_field(name="測試服", value="https://discord.gg/AXCZ8NPcSV", inline=True)
        embed.add_field(name="YT", value="https://www.youtube.com/channel/UCaIrAS2jmGz877k0pkvNQWA", inline=False)
        embed.add_field(name="Twitch", value="https://www.twitch.tv/sker001", inline=False)
        embed.set_footer(text="自主學習專用 ")
        await ctx.send(embed=embed)

    @commands.command()
    async def ero(self, ctx, *,msg):
        if  ctx.message.author.id == 403895664666214400:
            await ctx.message.delete()
            await ctx.send("@everyone "+str(msg))
        else:
            await ctx.send(f"你沒資格")

    @commands.command()
    async def clear(self, ctx, count:int):
        if  ctx.message.author.id == 403895664666214400:
            await ctx.channel.purge(limit=count+1)
        else:
            await ctx.send(f"你沒資格")

    @commands.command()
    async def check_TWtime(self,ctx):
        UTC0 = datetime.datetime.today()  # 獲得當地時間
        GMT8 = datetime.timedelta(hours=8)  # 時差
        TWTime = UTC0 + GMT8
        TWTime = TWTime.strftime("%H%M")
        await ctx.send(TWTime)

    @commands.command()
    async def check_time(self,ctx):
        await ctx.send(datetime.datetime.now().strftime("%H%M"))

def setup(bot):
    bot.add_cog(main(bot))