# Canvas-Bot

**DISCLAIMER:
This bot is for personal and private usage in its current state.**

---

## Description
This is a discord bot that makes use of the open Canvas api to remind students
on discord about their upcoming assignments and reminds them to check their
Canvas about more details about the assigments' due date. Using a mixture of
Python to create functions used in commands and for the bot and will be running
on AWS (Amazon Web Services) for hosting.

---
## Problem
How can we make a more efficient method to keep track of academic tasks through 
means of using a social platform?

## Solution
Due to the higher usage of Discord for communicating between students, caused by
recent pandemic and even before the pandemic, our group is creating a Discord bot 
that allows users to either add to their server or use  personally to keep 
themselves on track with their current academic assignments though messages from 
the bot.

---
## Prerequisites
The following libraries need to be installed. They can be installed with the following terminal commands:

`pip install discord`

`pip install canvas`

`pip install canvasapi`

**YOU HAVE TO CREATE A NEW CHANNEL IN YOUR SERVER CALLED "canvas"**
---
## TODO
1. Use python to make a bot
    - Issues:
        - Being able make a secrets.py file
        - Currently: personal usage
            - Planning: make the bot work further more for a server
        - Not everyones assignment is due on the same time

1. Make functions in the back-end to be used in bot commands
    - Use simple functions

1. Have the bot display the upcoming assignments and the due dates for registered
classes.

1. Run the bot on AWS (Amazon Web Services)