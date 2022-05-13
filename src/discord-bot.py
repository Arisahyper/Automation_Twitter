import discord
import setting

token = setting.DISCORD_TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print("ログインしました")


@client.event
async def on_message(message):
    channel = message.channel

    if message.author.bot:
        return

    if message.content == "hi":
        await channel.send(f"Hello! {message.author.name}")

    if message.content == "miko":
        with open("board.txt", mode="r") as f:
            message = f.read()
            try:
                await channel.send(message)
            except discord.errors.Forbidden as err:
                await channel.send(f"しっぱい: {err}")


# @client.event
# async def on_message(message):
#     if message.content.startswith("$thumb"):
#         channel = message.channel
#         await channel.send("Send me that 👍 reaction, mate")

#         def check(reaction, user):
#             return user == message.author and str(reaction.emoji) == "👍"

#         try:
#             reaction, user = await client.wait_for(
#                 "reaction_add", timeout=60.0, check=check
#             )
#         except TimeoutError:
#             await channel.send("👎")
#         else:
#             await channel.send("👍")


client.run(token)
