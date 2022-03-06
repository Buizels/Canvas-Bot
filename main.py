# Main file for the Discord Bot

from secrets import TOKEN, course_id
import discord
from discord.ext import commands
import canv
import os

client = commands.Bot(command_prefix = "!")


@client.event # Bot Status
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @bot.command(name = 'v')
# async def version(context):
#     myEmbed = discord.Embed(title ="Current Version", description="Bot Version: 1.0.0", color = 0x000000)
#     myEmbed.add_field(name = "Version Code:", value = "v1.0.0", inline=False)
#     myEmbed.add_field(name = "Date Released:", value = "March 6, 2022", inline=False)
#     myEmbed.set_footer(text ="Sample footer")
#     myEmbed.set_author(name = "Buizels")

#     await context.message.channel.send(embed = myEmbed)
#     return

# async def version(context):
#     myEmbed = discord.Embed(title = "Current Version", description = "Bot version: 1.0.0", coloe)
# @client.command()
# async def displayembed():
#     embed = discord.Embed(
#         title = "Title" , 
#         description = 'This is a description.' , 
#         color = discord.color.blue()
#     )

#     await client.say(embed=embed)

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} [{channel}]')

    if message.author == client.user:
        return

@client.command(name = 'v')
async def embedMessage(context):
    myEmbed = discord.Embed(title ="Current Version", description="Bot Version: 1.0.0", color = 0x000000)
    myEmbed.add_field(name = "Version Code:", value = "v1.0.0", inline=False)
    myEmbed.add_field(name = "Date Released:", value = "March 6, 2022", inline=False)
    # myEmbed.set_footer(text ="Sample footer")
    myEmbed.set_author(name = "Buizels")

    await context.message.channel.send(embed = myEmbed)
    return   



client.run(TOKEN)