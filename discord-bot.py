import discord
from discord import channel
import setting

token = setting.DISCORD_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    channel = message.channel

    if message.author.bot:
        return

    if message.content == "hi":
        await channel.send(f'Hello! {message.author.name}')

    if message.content == 'miko':
        with open("board.txt") as f:
            try:
                message = f.read()
                await channel.send(message)
            except:
                await channel.send("しっぱいしたにぇ...")

client.run(token)