import discord
import os
from google_images_search import GoogleImagesSearch
from io import BytesIO
from PIL import Image

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

    gis.search({'q': query})
    bytes=BytesIO()

    for image in gis.results():
      bytes.seek(0)
      raw_image_data=image.get_raw_data()
      image.copy_to(bytes, raw_image_data)
      bytes.seek(0)
      tmp_img=Image.open(bytes)
      tmp_img.save('my_image.jpg')
      file=discord.File('my_image.jpg')
      await message.channel.send('"'+image.url+'"', file=file)
 

client.run(os.getenv('Token'))