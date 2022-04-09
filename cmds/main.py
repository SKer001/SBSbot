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
        , timestamp=datetime.datetime.utcnow
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/693782101463400498/962316326196617267/cb182ac7a68575a5.png?size=4096")
        embed.set_author(
        name="幽靈夜閃"
        , url="https://github.com/SKer001"
        , icon_url="https://cdn.discordapp.com/attachments/693782101463400498/962316326196617267/cb182ac7a68575a5.png?size=4096")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/693782101463400498/962316326196617267/cb182ac7a68575a5.png?size=4096")
        embed.add_field(name="作者DC", value="幽靈夜閃#3443", inline=True)
        embed.add_field(name="測試服", value="https://discord.gg/UbvEP4PutR", inline=True)
        embed.add_field(name="YT", value="https://www.youtube.com/channel/UCaIrAS2jmGz877k0pkvNQWA", inline=False)
        embed.add_field(name="Twitch", value="https://www.twitch.tv/sker001", inline=False)
        embed.set_footer(text="自主學習專用 ")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(main(bot))