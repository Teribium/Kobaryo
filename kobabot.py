import discord
import youtube_dl
from discord.ext import commands

TOKEN = 'NTA3OTMwMjcyMzE5MTQzOTQ5.Dr33Kw.jQZ7FA-Ur89dB6UHOcI7_jGfMOw'
client = commands.Bot(command_prefix = ';')

players = {}
queues = {}
create_ytdl_player = {}

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='regarder '+str(len(client.servers))+' serveurs and '+str(len(set(client.get_all_members())))+' utilisateurs'))
    print('TR-002 is booting...')

@client.command()
async def kobaryohelp():
    await client.say('J to Join, L to Leave, P to Play, PS to Pause, ST to Stop and RS to Resume.')

@client.command(pass_context=True)
async def j(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def l(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def p(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, ytdl_options={'default_search': 'auto'})
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def ps(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def rs(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def st(ctx):
    id = ctx.message.server.id
    players[id].stop()

client.run(TOKEN)
