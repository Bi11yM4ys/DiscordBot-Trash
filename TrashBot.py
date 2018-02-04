import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("Connected to the Matrix")


@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Response!!" % (userID))
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

    if message.content.startswith("!amIcool"):
        await client.send_message(message.channel, "Of course, Why would he not")

    if message.content == "cool":
        await client.send_message(message.channel, ":cool:")
    if message.content.startswith("!hey"):
        await client.send_message(message.channel, "AND I SAY HEY! WHAT A WONDERFUL KIND OF DAY")
    if message.content == "robot":
        await client.send_message(message.channel, ":robot:")
    

client.run("") #TokenGoesHere
