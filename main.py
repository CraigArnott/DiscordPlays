import discord
import asyncio
import yaml

client = discord.Client()

'''Make backup saves every x seconds'''
async def backup(x):
    await asyncio.sleep(x)

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


with open('config.yaml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
backup_frequency = int(cfg['backup_frequency'])
token = cfg['token']
if(token == 'INSERT TOKEN HERE'):
    print('No token present in config file!')
    exit(-1)
client.loop.create_task(backup(backup_frequency))
client.run(token)
