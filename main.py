# Main file for the Discord Bot

from secrets import TOKEN, course_id
from discord.ext import commands
import discord
import canv



client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.command(name='v')
async def version(context):

    myEmbed = discord.Embed(title ="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="Feburary 1st, 2022", inline=False)
    myEmbed.set_footer(text ="Sample footer")
    myEmbed.set_author(name="Rafiul Islam")

    await context.message.channel.send(embed=myEmbed)

@client.event # Bot Status
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author ==  client.user:
        return

    if message.channel.name == 'testing':

        if user_message.lower() == '!anon':
            await message.channel.send(canv.get_anouncement(course_id))
            # await message.channel.send("\n")
            await message.channel.send(canv.get_anouncement_content(canv.get_anouncement(course_id).message))        

            return


        elif user_message.lower() == '!anons':
            await message.channel.send(canv.get_anouncements(course_id))

            return
        
        elif user_message.lower() == "!na": 
            await message.channel.send(canv.get_next_assignment(course_id))
            
            return
        
        elif user_message.lower() == "!nas":
            await message.channel.send(canv.get_anouncements(course_id))
            
            return

        elif user_message.lower() == "!gas":
            await message.channel.send(canv.get_all_assignments(course_id))
            return

client.run(TOKEN)