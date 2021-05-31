import os
import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()
trigger_words = ["science", "logic", "experience", "don't agree"]
happy_words = ["party", "drinks", "kingfisher","clubbing"]
uncle_arguments = "Don't talk back to elders you young disrespectful child, I have known since you were a magu, I have lived through war, what have you seen in your life apart from those stupid IPL which isn't even real cricket, respect elders and test cricket."
advice = ['stop texting girls, all problems will go away.','open kigfisher, jiyo befikar','friendzone is the best zone, because friend does not stop you from having drinks','all problems, one solution, marriage!','the day you start lying to your spouse will be the day you start living happy','I proposed to a girl, she rejected, I told that to my parents, they arranged marriage with same girl, share your problems with your parents, they will most definitely have a solution','Yoga solves all problems, verified from Whatsapp','first accept my Facebook friend request, then ask for advice']
@client.event
async def on_ready():
  print("you have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return 
  if msg.startswith(".commands"):
    await message.channel.send("use .hello to say hello to uncle\n use .advice to get an advice from uncle\n be careful there might be a few words that might trigger him and start a full fledged rant on you. One example is if you start using logic to argue with him. \n Uncle loves drinks, so if you use words that direct towards it he will get ready for a party. \n Uncle is lazy, so please don't ask for help, he won't. Don't believe me? Ask for help. \n Please don't wish him good morning or evening, he'll start sending cringy photos of him wishing you the same.")
  if msg.startswith('.hello'):
    await message.channel.send('Hello')
  if msg.startswith(".advice"):
    for i in range(len(advice)):
      await message.channel.send(str(i)+"."+" "+advice[i])
  if any(word in msg for word in trigger_words):
    await message.channel.send(uncle_arguments)
  if any(word in msg for word in happy_words):
    embed = discord.Embed(title="I am ready", color=discord.Color.purple())
    embed.set_image(url="https://crickettimes.com/wp-content/uploads/2019/10/Ravi-Shastri.png")
    await message.channel.send(embed=embed) 
    await message.channel.send(embed=embed)
  if "future" in msg:
    embed=discord.Embed(title="Future plans", url="https://www.jeevansathi.com", description="This is the only plan you should have for the future")
    await message.channel.send(embed=embed)
  if "good morning" in msg:
    embed = discord.Embed(title="Good Morning!", color=discord.Color.purple())
    embed.set_image(url="https://tailpic.com/wp-content/uploads/2019/04/35-Good-Morning-Quotes-and-Wishes-With-Beautiful-Images-29-735x600.jpg")
    await message.channel.send(embed=embed)
  if "good evening" in msg:
    embed = discord.Embed(title="Good Evening!", color=discord.Color.purple())
    embed.set_image(url="https://wishesmagazine.com/wp-content/uploads/2018/04/Good-Evening-Wishes-Image.jpg")
    await message.channel.send(embed=embed)
  if "trolling" in msg:
    embed = discord.Embed(title="To hell with those who troll", color=discord.Color.purple())
    embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_Jno-jFfXQhTgCbdS59BT2dDaNGP1w5SsX8rFPduyP572reQFx_bCtwYehEyDRjQQhcU&usqp=CAU")
    await message.channel.send(embed=embed)     
  if "help me" in msg:
    embed = discord.Embed(title="sorry! too tired", color=discord.Color.purple())
    embed.set_image(url="https://crickettimes.com/wp-content/uploads/2019/10/Ravi-Shastri.png")
    await message.channel.send(embed=embed)   






  
  
my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)
