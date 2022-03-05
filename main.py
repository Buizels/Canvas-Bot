# Main file for the Discord Bot

from secrets import TOKEN
import discord
import canv

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



client.run(TOKEN)