import discord
import os
# load our local env so we dont have the token in public
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
from core.classes import Cog_Extension



class music(Cog_Extension):

    @commands.command()
    async def join(self,ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
            ctx.send(f"Bot is connected")
        else:
            voice = await channel.connect()
            ctx.send(f"Bot is connected")

    @commands.command()
    async def leave(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
                await ctx.voice_client.disconnect()
                ctx.send(f"Bot is disconnected")


    @commands.command()
    async def play(self,ctx, url):
        YDL_OPTIONS = {"format": "bestaudio", "noplaylist": "True"}
        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info["url"]
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await ctx.send("Bot is playing")
        else:
            await ctx.send("Bot is already playing")
            return


    @commands.command()
    async def pause(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.pause()
            await ctx.send("Bot has been paused")
        elif not voice.is_playing():
            voice.resume()
            await ctx.send("Music is Continuous")

    @commands.command()
    async def stop(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.stop()
            await ctx.send("Stopping...")
    
    
def setup(bot):
    bot.add_cog(music(bot))