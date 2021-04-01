import discord
import os
from google_images_search import GoogleImagesSearch


client =discord.Client()
gis= GoogleImagesSearch(os.getenv('api_key'), os.getenv('search_engine'))


@client.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))

@client.event
async def on_message(message):
  if message.author ==client.user:
    return
 
  if message.content.startswith('!img'):
    string=message.content
    query=string[4:]
    filetype='jpg|png'

    gis.search({'q': query, 'filetype':filetype})
    

    for image in gis.results():
      await message.channel.send(image.url)
 

client.run(os.getenv('Token'))