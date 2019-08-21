from SecretKey import *
import discord
from discord.utils import get


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#@client.event
#async def on_message(message):
 #   if message.author == client.user:
  #      return

   # if message.content.startswith('$hello'):
    #    await message.channel.send('Hello!')
        
    #channelID = message.channel.id   
    #channel = client.get_channel(channelID)
    #await channel.send(message.content)

@client.event
async def on_message(message):
    # gets the guild
    guild = message.guild
    # user uses !Roles command to print a list of available roles on the server
    if message.content.startswith('!Roles'): 
        role_id_list = [598882204843769856, 598882290759892997]
        
        for role_id in role_id_list:
            role = get(guild.roles, id = role_id)
            channelID = message.channel.id   
            channel = client.get_channel(channelID)
            await channel.send(role, role.color)

        
#hello james

client.run(secret) 



# [598882204843769856, 598882290759892997]