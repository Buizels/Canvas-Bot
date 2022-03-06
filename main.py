# Main file for the Discord Bot

from secrets import TOKEN, course_id
import discord
from discord.ext import commands
import canv
import os
from dateutil import parser

bot = commands.Bot(command_prefix="!")

@bot.event # Bot Status
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(name = 'h')
async def embedMessage(context):
    embed=discord.Embed(title="Canvas Bot ", description="Help Commands", color=0xd35650)
    embed.add_field(name="!v", value="Bot Version", inline=False)
    embed.add_field(name="!anon", value="Announcement", inline=False)
    embed.add_field(name="!anons", value="Multiple Announcements", inline=False)
    embed.add_field(name="!gna", value="Next Assignment", inline=False)
    embed.add_field(name="!nas", value="Next Multiple Assignments", inline=True)
    embed.set_footer(text="!h for Canvas Bot Commands")
    await context.send(embed=embed)
    return


@bot.command(name = 'v')
async def embedMessage(context):
    myEmbed = discord.Embed(title ="Current Version", description="Bot Version: 1.0.0", color = 0x000000)
    myEmbed.add_field(name = "Version Code:", value = "v1.0.0", inline=False)
    myEmbed.add_field(name = "Date Released:", value = "March 6, 2022", inline=False)
    # myEmbed.set_footer(text ="Sample footer")
    myEmbed.set_author(name = "Buizels")

    await context.message.channel.send(embed = myEmbed)
    return   

@bot.command(name = 'anon') #gets anouncement
async def embedMessage(message):
    if message.channel.name == 'canvas':
        await message.channel.send(canv.get_anouncement(course_id))
        await message.channel.send(canv.get_anouncement_content(canv.get_anouncement(course_id).message))        

        return

@bot.command(name = 'anons') #gets anouncements, ERROR
async def embedMessage(message):
    if message.channel.name == 'canvas':

        list_announcements = []
        announcement = canv.get_anouncements(course_id)
        for i in announcement:
            list_announcements += [i.title]

        # Print first 3 assignments
        for i in range(3):
            await message.channel.send(list_announcements[i])    

        return

@bot.command(name = 'gna') #gets next assignment
async def embedMessage(message):
    if message.channel.name == 'canvas':
        next_assign = canv.get_next_assignment(course_id)
        await message.channel.send(next_assign.name + " is due at: " + str(next_assign.due_at))        

        return

@bot.command(name = 'nas') #get next multiple assignments
async def embedMessage(message):
    if message.channel.name == 'canvas':
        next_assignments = canv.get_next_assignments(course_id)
        for i in next_assignments:
            await message.channel.send(i.name + " is due at: " + str(i.due_at))      
        next_assigns = canv.get_next_assignments(course_id)
        string = ''
        for i in  next_assigns:
            string += str(i.name) + " is due at: " + str(canv.convert_to_pst(i.due_at)) + "\n"

        await message.channel.send(string)
        return

# !TODO
# @bot.command(name = 'gas') #gets all assignments, ERROR
# async def embedMessage(message):
#     if message.channel.name == 'testing':
#         next_assigns = canv.get_all_assignments(course_id)
#         string = ''
#         for i in  next_assigns:
#             string += str(i.name) + " is due at: " + str(canv.convert_to_pst(i.due_at)) + "\n"

#         await message.channel.send(string)
#         return

bot.run(TOKEN)