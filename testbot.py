from SecretKey import *
import discord
from discord.ext import commands
from discord.utils import get
import discord.utils



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


# arg1 is role name and arg2 is role color
# user types $CreateRole to trigger
# user needs to add "" around any role that is more than 1 word
# need manage roles premission -- just give admin


@client.command(pass_context = True)
async def CreateRole(ctx,arg1):
    RoleName = arg1
    #RoleColor = arg2
    # gets the author of the message
    author = ctx.message.author
    # has the server create a role within the server
    await author.create_role(author.guild, name = RoleName)
    # 
    role = discord.utils.get(author.guild.roles, name = RoleName)
    # adds the role to the user
    await author.add_roles(role)
    







# enter a comand to create a role and assign it a hex value
# both are user inputs       
#hello james

client.run(secret) 



# [598882204843769856, 598882290759892997]