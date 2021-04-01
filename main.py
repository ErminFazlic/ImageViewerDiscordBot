import discord
import os
client =discord.Client()

@client.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))

@client.event
async def on_message(message):
  if message.author ==client.user:
    return
 

  
  if message.content.startswith('$play'):
    await message.channel.send('!play toto africa')
 

client.run(os.getenv('Token'))