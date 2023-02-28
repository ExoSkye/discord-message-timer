import datetime

import discord
from discord.ext import tasks
import sys

CHANNEL_ID = int(sys.argv[1])
MINUTES = int(sys.argv[2])

client = discord.Client(intents=discord.Intents.messages)


@tasks.loop(minutes=5)
async def purge():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    async for message in channel.history():
        if message.created_at < datetime.datetime.now() - datetime.timedelta(minutes=MINUTES):
            await message.delete()

with open(".token") as f:
    client.run(f.read().strip())
