# Main file for the Discord Bot

from secrets import TOKEN
import discord
import canv

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event()
async def on_ready():
    username = str(message.author).split('#')[0]
    user_message = str(message.contect)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author ==  client.user:
        return

    if message.channel.name == 'testing':
        if user_message.lower() == 'hello':
            await message.channe.send(f'fuck you {username}')

client.run(TOKEN)