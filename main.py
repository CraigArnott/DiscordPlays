# sample code taken from https://github.com/Rapptz/discord.py

import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # bot should ignore its own messages
    if(message.author == client.user):
        return

    if str(message.channel) == 'discordplays':
        await client.send_message(message.channel, 'Welcome to Discord Plays!')

token = open('token.txt').readline().strip()
client.run(token)
