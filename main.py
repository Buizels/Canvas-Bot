# Main file for the Discord Bot

from secrets import TOKEN, course_id
import discord
from discord.ext import commands
import canv
import os

bot = commands.Bot(command_prefix="!")

@bot.event # Bot Status
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(name = 'v')
async def embedMessage(context):
    myEmbed = discord.Embed(title ="Current Version", description="Bot Version: 1.0.0", color = 0x000000)
    myEmbed.add_field(name = "Version Code:", value = "v1.0.0", inline=False)
    myEmbed.add_field(name = "Date Released:", value = "March 6, 2022", inline=False)
    # myEmbed.set_footer(text ="Sample footer")
    myEmbed.set_author(name = "Buizels")

    await context.message.channel.send(embed = myEmbed)
    return   

@bot.command(name = 'anon')
async def embedMessage(message):
    if message.channel.name == 'testing':
        await message.channel.send(canv.get_anouncement(course_id))
        await message.channel.send(canv.get_anouncement_content(canv.get_anouncement(course_id).message))        

        return

    # myEmbed = discord.Embed(title = "Anouncement", color = 0x000000)
    # title = str(canv.get_anouncement(course_id))
    # text = str(canv.get_anouncement_content(canv.get_announcement(course_id).message))

    # myEmbed.add_field(name = title, value = text)



bot.run(TOKEN)