import discord
import os
import random

from discord.ext import commands
from ek_calisma import yazı_tura
from ders2_1 import sifre_olusturucu
from r_duck import get_duck_image_url
from jeton import jeton



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def toplama(ctx,a = 1, b = 2):
    await ctx.send(a + b)

@bot.command()
async def carpma(ctx,a = 1, b = 2):
    await ctx.send(a * b)

@bot.command()
async def yazı_tura_o(ctx):
    await ctx.send(yazı_tura())

@bot.command()
async def sifre(ctx, lt = 4):
    await ctx.send(sifre_olusturucu(lt))

@bot.command()
async def mem(ctx):
    with open('C:/Users/Mehmet Ali Öncü/Desktop/pro/images/mem.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('C:/Users/Mehmet Ali Öncü/Desktop/pro/images/mem2.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open('C:/Users/Mehmet Ali Öncü/Desktop/pro/images/mem3.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem_r(ctx):

    choice = random.choice(os.listdir("C:/Users/Mehmet Ali Öncü/Desktop/pro/images"))

    with open(f'C:/Users/Mehmet Ali Öncü/Desktop/pro/images/{choice}', 'rb') as mems:
            mem_ = discord.File(mems)

            await ctx.send(file=mem_)

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)



bot.run(jeton)