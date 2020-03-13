import os  # import module for directory management
from dotenv import load_dotenv  # load module for usage of a .env file
import subprocess  # import module used to do linux code execution
from discord.ext import commands  # import  command module from discord.py
import discord  # import discord.py module
import scoreboard as sc  # import scoreboard.py

bot = commands.Bot(command_prefix=('ig ', 'Ig '))  # set the command prefix

load_dotenv()  # load the .env file containing id's that have to be kept secret for security
token = os.getenv('DISCORD_TOKEN')  # get our discord bot token from .env

DEFENSE_MESSAGE = True  # if true, bot won't  speak to itself

ugly = ['JeSuisLelijk', 'jesuislelijk']


# print a message when the bot starts
# async will make sure the different functions can run simultaneously
@bot.event  # checks for bot events
async def on_ready():  # run when bot is ready
    print('Bot connected!')


# check messages when they're send and answer if something triggers the bot
@bot.event
async def on_message(message):  # run when a message has been send
    global DEFENSE_MESSAGE  # create a global variable
    # makes sure we don't fire on ourselves
    if message.author.name == 'Ingenium':
        return

    # if the message contains jesuislelijk with or without caps respond the response
    for item in ('JeSuisLelijk', 'jesuislelijk'):
        if item in message.content:
            """await will wait and trigger when only if the if statement is true"""
            await message.channel.send('I love Nanor and Toot')  # delete the message after 100 sec

    for item in ('Stormloop', 'stormloop'):
        if item in message.content:
            """await will wait and trigger when only if the if statement is true"""
            await message.channel.send('The biggest pimp ever')  # delete the message after 100 sec

    # if the message contains 69 answer nice
    if '69' in message.content:
        if '<' in message.content:
            """correct for possible emoji's containing 69"""
            pass
        else:
            response = 'Nice'
            await message.channel.send(response)

    # if the message contains 420 answer Haha Weeeeeeed!
    if '420' in message.content:
        if '<' in message.content:
            """correct for possible emoji's containing 69"""
            pass
        else:
            response = 'Haha Weeeeeeed!'
            await message.channel.send(response)

    # pay respect when someone types F or f
    if message.content in ('F', 'f'):
        response = 'The Ingenium server pays their respect'
        await message.channel.send(response)

    # respond to oof
    if message.content in ('Oof', 'oof'):
        response = 'Oof you done goofed son'
        await message.channel.send(response)

    # respond to happy birthday
    if message.content.find('happy birthday') != -1 or message.content.find('Happy Birthday') != -1:
        response = 'Ingenium wishes you a happy birthday! 🎈🎉'
        await message.channel.send(response)

    await bot.process_commands(message)


# when a new player joins, write the message
@bot.event
async def on_member_join(member):
    # define the channel id's for the different channels it wants to mention
    welcome = bot.get_channel(611184121024086016)
    how_to_apply = bot.get_channel(677626692335960064)
    self_roles = bot.get_channel(611188046339244032)
    server_rules_and_info = bot.get_channel(611184197041651718)
    general_chat = bot.get_channel(611184705693417472)

    # mention with .mention, \n will add a newline in the f string
    response = (f'Hi {member.mention}, welcome to the Ingenium Discord server!. \n'
                f'You can find our rules as well as other information about the server in {server_rules_and_info.mention}. \n'
                f'If you want to apply, head over to {how_to_apply.mention} and follow the instructions. \n'
                f'Let us know where you are from in in {self_roles.mention}. \n'
                f'Feel free to introduce yourself in {general_chat.mention}. \n'
                f'\n'
                f'If you have any questions feel free to ask our staff about it! \n'
                f'We hope you will have a pleasant time on the server!')
    await welcome.send(response)


# set defferent commands the bot will respond to
# name sets the commands name, help will trigger at ig help
@bot.command(name='test', help='test if the bot is working')
async def test_bot(ctx):
    response = 'Don\'t worry, I\'m working!'
    await ctx.send(response)


# write the server status to the channel
@bot.command(name='status', help='check the server status')
async def status(ctx):
    result = subprocess.run(['mscs', 'status'], stdout=subprocess.PIPE)  # execute mscs status in linux console
    result.stdout.decode('utf-8')
    await ctx.send(result)


# scoreboard command
scoreboard_help = f'print the scoreboard you want to get to the chat. '
@bot.command(name='scoreboard', help=scoreboard_help)
async def scoreboard(ctx, arg, arg2=''):
    result = sc.display(arg, arg2)  # get result from the scoreboard display function
    await ctx.send(result)


# command to fetch scoreboard data of a single player and a single scoreboard
@bot.command(name='playerscore', help='display a single score for a player')
async def playerscore(ctx, arg, arg2):
    result = sc.player(arg, arg2)
    print(result)
    await ctx.send(result)

bot.run(token)
