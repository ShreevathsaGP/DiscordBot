# imports
import os
import time
import discord
import unicodedata
from solver import *
from credentials import *

# globals
send_trigger = "!VathsaBot"
client = discord.Client()

# bot state
class BotState:
    def __init__(self):
        self.chat_history = [None, None]
        self.chat_index = 0
        self.send_backlog = []
bot_state = BotState()

# trigger function
def check_trigger(history):
    if history[0] == None or history[1] == None:
        return False, -1

    if history[0].find("scramble") != -1 and history[1].find("The word is") != -1:
        return True, 1

    if history[1].find("scramble") != -1 and history[0].find("The word is") != -1:
        # print("True")
        return True, 0

    return False, -1

# extract scramble
def extract_word(string):
    length = len("The word is")
    index = string.find("The word is")
    if index == -1:
        return None

    start_index = index + length + 1
    end_index = string.find(",") - 1

    if start_index == -1 or end_index == -1:
        return None

    return string[start_index:end_index + 1]

# message evaluation
@client.event
async def on_message(message):
    if bot_state.chat_index == 0:
        bot_state.chat_index = 1
    else:
        bot_state.chat_index = 0

    content = message.content
    content = str(unicodedata.normalize('NFKD', content).encode('ascii', 'ignore'))
    bot_state.chat_history[bot_state.chat_index] = content
    # print(content)

    if message.content.find(send_trigger) != -1:
        await message.channel.send("leave me alone")
    
    check, index = check_trigger(bot_state.chat_history)
    if check:
        word = extract_word(bot_state.chat_history[index])
        if word != None:
            for word in solve_scramble(word):
                bot_state.send_backlog.append(word)

    if len(bot_state.send_backlog) != 0:
        await message.channel.send(bot_state.send_backlog.pop())

# run client
client.run(bot_token)
