import os
import discord
import random
import requests
from discord.ext import commands
from keep_alive import keep_alive
from replit import db


client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
  print('We\'re online!. We have logged in as {0.user}'.format(client))

@client.command()
async def say(ctx, message):
  await ctx.send(message)

@client.command()
async def info(ctx):
  await ctx.send('Commands must start with the $ symbol \n`$info` : Displays available commands\n`$price [insert crypto name]` : Displays current price of coin\n`$list` : Displays all valid coins')

@client.command()
async def price(ctx, coin):
  URL='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
  r = requests.get(url=URL)
  data = r.json()
  coin = coin.lower()

  exString = "bytecoin"

  for i in range(len(data)):
    db[data[i]['id']] = data[i]['current_price']

  if coin in db.keys():
    await ctx.send("USD Value of " + coin + " is:")
    await ctx.send(db[coin])
  elif coin in exString:
    await ctx.send('USD: All the money!!!')
  else:
    await ctx.send('That crypto does not exist!')

@client.command()
async def list(ctx):
  coinList = [key for key in db.keys()]
  await ctx.send(coinList)



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if (message.content.startswith(' ')):
    return
    
  if ('among us' in message.content):
    await message.channel.send('SUS?????')
    return

  if ('hello' in message.content):
    await message.channel.send('Hello!')
    return

  if ('command' in message.content or 'help' in message.content):
    await message.channel.send('Try typing "$info"!')
    return

  await client.process_commands(message)  # this is necessary or the bot won't read commands
 

keep_alive()
client.run(os.environ['TOKEN'])
