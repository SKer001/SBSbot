from email.contentmanager import raw_data_manager
from http.client import ImproperConnectionState
import discord
from discord.ext import commands
import json
import random
import os
import time
from PIL import Image


#intens為特殊權限管理 member要額外開
intents = discord.Intents.default()
intents.members = True
intents.presences = True

with open("../setting.json",mode="r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

#BOT指令為$
bot = commands.Bot(command_prefix='$',intents = intents,help_command=None)

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


#bad apple#############################################################################
CLIP_FRAMES = 6571

CLIP_LENGTH = 219.0666

ASCII_CHARS = ['⠀','⠄','⠆','⠖','⠶','⡶','⣩','⣪','⣫','⣾','⣿']
ASCII_CHARS.reverse()
ASCII_CHARS = ASCII_CHARS[::-1]

WIDTH = 60

TIMEOUT = 1/((int(CLIP_FRAMES/1)+1)/CLIP_LENGTH)*18

def resize(image, new_width=WIDTH):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int((aspect_ratio * new_width)/2)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image

def grayscalify(image):
    return image.convert('L')

def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def do(image, new_width=WIDTH):
    image = resize(image)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    new_image = [pixels[index:index+int(new_width)] for index in range(0, len_pixels, int(new_width))]

    return '\n'.join(new_image)

def runner(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in",path)
        return
    image = do(image)

    return image

frames = []

for i in range(0, int(CLIP_FRAMES/4)+1):
    path = "./frames/frame"+str(i*4)+".jpg" #<--- path to folder containing every frame of the video
    frames.append(runner(path))

@bot.command()
async def BadApple(ctx):  
    oldTimestamp = time.time()

    start = oldTimestamp

    seconds = 0
    minutes = 0

    i = 0
        
    while i < len(frames)-1:
        disp = False
        while not disp:
            newTimestamp = time.time()
            if (newTimestamp - oldTimestamp) >= TIMEOUT:

                await ctx.message.channel.send(frames[int(i)])
                    
                newTimestamp = time.time()

                i += (newTimestamp - oldTimestamp)/TIMEOUT
                    
                oldTimestamp = newTimestamp

                disp = True
########################################################################
                    
#RUNbot
if __name__ == "__main__":
    bot.run(jdata["TOKEN"])