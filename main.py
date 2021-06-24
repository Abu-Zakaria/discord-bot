import os
import discord
from dotenv import load_dotenv 

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
  print("bot ready!")
  print(f"bot username: {client.user}")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("/hello-bot"):
    await message.channel.send("Hello there!")
  
client.run(os.getenv("TOKEN"))
