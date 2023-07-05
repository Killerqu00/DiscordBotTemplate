import discord
import logging
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    logging.info(f"Logged as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

with open("creds.json") as f:
    TOKEN = json.loads(f.read())["token"]
client.run(TOKEN)
