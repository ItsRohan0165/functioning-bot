import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Hex')
 


@client.event
async def on_message(message):
    if message.content == '!hq':
        await client.send_message(message.channel,'`` The bot is under development``')
    if message.content == '!pmsg':
        await client.send_message(message.channel,' @everyone \n ```The bot is currently under development. It is expected to work within a week.``` \n **We hope you understand.** \n  The Bot   wroks for \n ``Hq``\n `` Confetti`` only.   ')
   

    if message.content == '!pingall':
        await client.send_message(message.channel,'@everyone')
    if message.content == '!pinghere':
        await client.send_message(message.channel,'@here')
    if message.content == '!confetti':
        await client.send_message(message.channel,'The bot is under development. ')
    if message.content == '!wwf':
        await client.send_message(message.channel,'Sorry! Words With Friends Live is not currently available.')
    if message.content == '!details':
        await client.send_message(message.channel,'The owner of the bot is ``Guru`` and developed  by `` Playing with $wift code`` ')
    if message.content.startswith('!coinflip'):
        randomlist = ['heads','tails','heads',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!pingme'):
        await client.send_message(message.channel,'hey !! <@%s> Wake up!! buddy'  %(message.author.id))
    if ('fuck,bitch,sex,madarchod,behnchod') in message.content:
       await client.delete_message(message)
    if message.content == '!invite':
        await client.send_message(message.channel,'https://discord.gg/eMy2GvT')
client.run('NTE3NzAzNDYxNzQ4MzQyODE2.XKSIoA.jsu-mMwCp8Wm2Md7zwVjT0nEhv8')
 
