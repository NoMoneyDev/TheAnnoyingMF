from importlib.machinery import WindowsRegistryFinder
from sqlite3 import connect
from tracemalloc import stop
from webbrowser import get
from aiohttp import request
import discord
from discord.ext  import commands
import random
import time
import randfacts
import youtube_dl
import ffmpeg


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="oof ", intents=intents)



  
@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready. ")




@bot.command(pass_context = True)
async def test(ctx):
  await ctx.send("You are <@" + str(ctx.author.id) + "> ")


@bot.command(pass_context = True)
async def Help(ctx):
  help =   str(("TheAnoyyingMF commands :") + ("\n") +
          ("Prefix = oof ") + ("\n") +
          ("join = Join your voice channel") + ("\n") +
          ("leave = Leave your voice channel") + ("\n") +
          ("play(url) = play your url on youtube") + ("\n") +
          ("facts = send you random facts") + ("\n") +
          ("wordrace = race with your friend who type the fastest") + ("\n") +
          ("m8ball(question) = 8ball") + ("\n") + ("\n") +
          ("Voice troll yo friend :") + ("\n") +
          ("FBI, doorknock, spike, bomb, apexknock") + ("\n")
          )
  await ctx.send(help)


@bot.command(pass_context = True)
async def join(ctx):
  if (ctx.voice_client):
    await ctx.send("Bruh I'm right here")
  
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
  else :
    await ctx.send("You aren't even in a channel bruv")


@bot.command()
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
  else :
    await ctx.send("I'm not even there bruh")


"""
@bot.event
async def on_voice_state_update(member, before, after):
  if before.channel is None and after.channel is not None:
    print("you joined")
    
    await connect(Voice_ID)
"""


# Misc CMD

# randomFact
@bot.command(pass_context = True)
async def facts(ctx):
  fact = randfacts.get_fact()
  await ctx.send(fact)

# 8 Ball
@bot.command(pass_context = True)
async def m8ball(ctx):
  answer = random.randint(1,10)
  ans = ["Hell Nah", "What are you thinking?", "Meh 50 50", "Idk. Good Luck", "Go for it bruv", "Yess, Go!", "Absolutely Yes", "Yup!", "Subarashi desu", "Mamamia, Yes"]
  await ctx.send(ans[answer])

# wordrace



@bot.command(pass_context = True)
async def wordrace(ctx):

    sentence = [
      "She doesn’t study German on Monday."
      ,"Does she live in Paris?"
      ,"He doesn’t teach math."
      ,"Cats hate water."
      ,"Every child likes an ice cream."
      ,"My brother takes out the trash."
      ,"The course starts next Sunday."
      ,"She swims every morning."
      ,"I don’t wash the dishes."
      ,"We see them every week."
      ,"I don’t like tea."
      ,"When does the train usually leave?"
      ,"She always forgets her purse."
      ,"You don’t have children."
      ,"I and my sister don’t see each other anymore."
      ,"They don’t go to school tomorrow."
      ,"He loves to play basketball."
      ,"He goes to school."
      ,"The Earth is spherical."
      ,"Julie talks very fast."
      ,"My brother’s dog barks a lot."
      ,"Does he play tennis?"
      ,"The train leaves every morning at 18 AM."
      ,"Water freezes at 0C"
      ,"I love my new pets."
      ,"We drink coffee every morning."
      ,"My Dad never works on the weekends."
      ,"She doesn’t teach chemistry."
      ,"I do love my new pets."
      ,"Mary brushes her teeth twice a day."
      ,"He drives to work."
      ,"Mary enjoys cooking."
      ,"She likes bananas."
      ,"My mother never lies."
      ,"You don’t listen to me."
      ,"I run four miles every morning."
      ,"They speak English at work."
      ,"The train does not leave at 12 AM."
      ,"I have no money at the moment."
      ,"Do they talk a lot?"
      ,"Tomorrow early morning first I go to morning walk."
      ,"Does she drink coffee?"
      ,"You run to the party."
      ,"You have some schoolwork to do."
      ,"She doesn’t use a computer."
      ,"It snows a lot in winter in Russia."
      ,"We live in Texas."
      ,"You go to holiday every summer."
      ,"Do you like spaghetti?"
      ,"My daughter does the laundry."
    ]


    num = random.randint(1,(len(sentence)-1))

    global wr_start
    global word

    wr_start = 1
    word = sentence[num]
    await ctx.send("oof wr " +  word)


        

@bot.command(pass_context = True)
async def wr(ctx,*,attmp):
  
  global word

  if attmp == word:
    winner = ctx.author
    await ctx.send("Winner is <@" + str(winner.id) + ">")
    word = ""
  


  
# Troll CMD Rework Later Cuz too much work


@bot.command(pass_context = True)
async def play(ctx, url):
  server = ctx.message.guild
  voice_channel = server.voice_client

  if (ctx.voice_client) == None:
    await ctx.send("Let me in yo VC first")
    return

  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  YDL_OPTIONS = {'format':"bestaudio"}
  

  with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
    info = ydl.extract_info(url, download=False)
    url2 = info['formats'] [0] ['url']
    voice_channel.play(discord.FFmpegPCMAudio(executable =  "D:\Download\\ffmpeg-5.0-essentials_build\\ffmpeg-5.0-essentials_build\\bin\\ffmpeg.exe", source = url2, **FFMPEG_OPTIONS))
    voice_channel.is_playing()




@bot.command(pass_context = True)
async def FBI(ctx):
  server = ctx.message.guild
  voice_channel = server.voice_client
  if ctx.voice_client == None:
    await ctx.send("Let me in yo VC first")
    return
  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  YDL_OPTIONS = {'format':"bestaudio"}

  with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
    info = ydl.extract_info("https://www.youtube.com/watch?v=vTUP8eimDuY", download=False)
  url = info['formats'] [0] ['url']
  voice_channel.play(discord.FFmpegPCMAudio(executable =  "D:\Download\\ffmpeg-5.0-essentials_build\\ffmpeg-5.0-essentials_build\\bin\\ffmpeg.exe", source = url, **FFMPEG_OPTIONS))
  voice_channel.is_playing()
  voice_channel.source = discord.PCMVolumeTransformer(voice_channel.source)
  voice_channel.source.volume = 0.05

@bot.command(pass_context = True)
async def doorknock(ctx):
  server = ctx.message.guild
  voice_channel = server.voice_client
  if ctx.voice_client == None:
    await ctx.send("Let me in yo VC first")
    return
  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  YDL_OPTIONS = {'format':"bestaudio"}

  with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
    info = ydl.extract_info("https://www.youtube.com/watch?v=GX5cHG90ctA", download=False)
  url = info['formats'] [0] ['url']
  voice_channel.play(discord.FFmpegPCMAudio(executable =  "D:\Download\\ffmpeg-5.0-essentials_build\\ffmpeg-5.0-essentials_build\\bin\\ffmpeg.exe", source = url, **FFMPEG_OPTIONS))
  voice_channel.is_playing()


@bot.command(pass_context = True)
async def spike(ctx):
  server = ctx.message.guild
  voice_channel = server.voice_client
  if ctx.voice_client == None:
    await ctx.send("Let me in yo VC first")
    return
  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  YDL_OPTIONS = {'format':"bestaudio"}

  with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
    info = ydl.extract_info("https://www.youtube.com/watch?v=Gg_9QurvK6g", download=False)
  url = info['formats'] [0] ['url']
  voice_channel.play(discord.FFmpegPCMAudio(executable =  "D:\Download\\ffmpeg-5.0-essentials_build\\ffmpeg-5.0-essentials_build\\bin\\ffmpeg.exe", source = url, **FFMPEG_OPTIONS))
  voice_channel.is_playing()

@bot.command(pass_context = True)
async def bomb(ctx):
  server = ctx.message.guild
  voice_channel = server.voice_client
  if ctx.voice_client == None:
    await ctx.send("Let me in yo VC first")
    return
  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  YDL_OPTIONS = {'format':"bestaudio"}

  with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
    info = ydl.extract_info("https://www.youtube.com/watch?v=llCmtgvIqcY", download=False)
  url = info['formats'] [0] ['url']
  voice_channel.play(discord.FFmpegPCMAudio(executable =  "D:\Download\\ffmpeg-5.0-essentials_build\\ffmpeg-5.0-essentials_build\\bin\\ffmpeg.exe", source = url, **FFMPEG_OPTIONS))
  voice_channel.is_playing()


@bot.command(pass_context = True)
async def apexknock(ctx):
  server = ctx.message.guild
  voice_channel = server.voice_client
  if ctx.voice_client == None:
    await ctx.send("Let me in yo VC first")
    return
  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  YDL_OPTIONS = {'format':"bestaudio"}

  with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
    info = ydl.extract_info("https://www.youtube.com/watch?v=oVzvX_nk79g", download=False)
  url = info['formats'] [0] ['url']
  voice_channel.play(discord.FFmpegPCMAudio(executable =  "D:\Download\\ffmpeg-5.0-essentials_build\\ffmpeg-5.0-essentials_build\\bin\\ffmpeg.exe", source = url, **FFMPEG_OPTIONS))
  voice_channel.is_playing()

  voice_channel.source = discord.PCMVolumeTransformer(voice_channel.source)
  voice_channel.source.volume = 0.6


bot.run('MY_TOKEN')