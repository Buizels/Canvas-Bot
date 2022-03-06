# Main file for the Discord Bot

from secrets import TOKEN, course_id
import discord
import canv


client = discord.Client()

@client.event
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

        # announcement code           
        elif user_message.lower() == "!na": 
            await message.channel.send(canv.get_next_assignment(course_id))
            return
        
        elif user_message.lower() == "!nas":
            await message.channel.send(canv.get_next_assignments(course_id)(course_id))
            return
        
        


client.run(TOKEN)