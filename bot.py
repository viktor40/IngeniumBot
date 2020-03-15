import os  # import module for directory management
from dotenv import load_dotenv  # load module for usage of a .env file
import subprocess  # import module used to do linux code execution
from discord.ext import commands  # import the commands module from discord.py
from discord.ext import tasks  # import  command module from discord.py
import player_data as pd  # import the script to get player data
import discord  # import discord.py module
import scoreboard as sc  # import scoreboard.py
from filetail import FileTail  # import the script to tail files like in linux
import concurrent.futures as features  # import concurrent.features for the executor for the chat link

from server_data import CHAT_LINK_CHANNEL
from server_data import console_in
from server_data import console_out
from server_data import seed
from server_data import server_locations
from server_data import ips

bot = commands.Bot(command_prefix=('ig ', 'Ig '))  # set the command prefix

load_dotenv()  # load the .env file containing id's that have to be kept secret for security
token = os.getenv('DISCORD_TOKEN')  # get our discord bot token from .env

# if true, bot won't  speak to itself
DEFENSE_MESSAGE = True

ugly = ['JeSuisLelijk', 'jesuislelijk']


@bot.event
async def on_ready():
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
            # delete the message after 100 sec
            await message.channel.send('I love Nanor and Toot', delete_after=20)

    for item in ('Stormloop', 'stormloop'):
        if item in message.content:
            """await will wait and trigger when only if the if statement is true"""
            await message.channel.send('The biggest pimp ever', delete_after=60)  # delete the message after 60 sec

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
    if 'happy birthday' in message.content or 'Happy Birthday' in message.content:
        response = 'Ingenium wishes you a happy birthday! 🎈🎉'
        await message.channel.send(response)

    if 'ilmango' in message.content:
        response = 'Mango, Mango, Mango mango mango, Mangooooooooooooooooooooooooooooooooooooooooooo'
        await message.channel.send(response, delete_after=30)

    if 'stop lazy' in message.content:
        response = 'stop being lazy prick'
        await message.channel.send(response, delete_after=35)

    if 'Stop lazy' in message.content:
        response = 'stop being lazy prick'
        await message.channel.send(response, delete_after=35)

    if message.channel.id == CHAT_LINK_CHANNEL:
        msg = message.content
        sender = message.author
        with open("../mscs/worlds/survival/console.in", 'w') as f:
            f.writelines('tellraw @a [\"dc: <{}> {}\"]\n'.format(str(sender)[:-5], str(msg)))
            f.close()
            await bot.process_commands(message)

    await bot.process_commands(message)


# when a new player joins, write the welcome message
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


# commands everyone can uses
# set different commands the bot will respond to
# name sets the commands name, help will trigger at ig help
@bot.command(name='test', help='test if the bot is working')
async def test_bot(ctx):
    response = 'Don\'t worry, I\'m working!'
    await ctx.send(response)


# scoreboard command
scoreboard_help = f'print the scoreboard you want to get to the chat. '
@bot.command(name='scoreboard', help=scoreboard_help)
async def scoreboard(ctx, objective, number=''):
    result = sc.display(objective, number)  # get result from the scoreboard display function
    await ctx.send(result)


# command to fetch scoreboard data of a single player and a single scoreboard
@bot.command(name='playerscore', help='display a single score for a player')
async def playerscore(ctx, objective, player):
    result = sc.player(objective, player)
    await ctx.send(result)


@bot.command(name='seed', help='Display the server\'s seed')
async def show_seed(ctx):
    result = seed
    await ctx.send(f'`{result}`')


# commands only Members and Trial Member can use
@bot.command(name='mob_bot', help='spawn the mob bot')
@commands.has_any_role('Member', 'Trial Member')
async def spawn_mob(ctx):
    result = 'This command doesn\'t work yet'
    await ctx.send(result)


@bot.command(name='ip', help='spawn the mob bot')
@commands.has_any_role('Member', 'Trial Member')
async def show_ip(ctx, server):
    result = ips[server]
    await ctx.send(f'`{result}`')


@bot.command(name='location', help='show the nether portal coordinates of something')
@commands.has_any_role('Member', 'Trial Member')
async def spawn_mob(ctx, *locations):
    location = ''
    for l in locations:
        location += l + ' '
    location = location[:-1]
    location = location.replace('_', ' ')
    result = server_locations[location.lower()]
    await ctx.send(f'`{location.lower()} nether roof coordinates: {result}`')


# link the minecraft ign to the discord name
# pass_context makes sure we can read info like message sender and more
@bot.command(name='link_name', help='link minecraft ign to discord screen name', pass_context=True)
@commands.has_any_role('Member', 'Trial Member')
async def link_name(ctx, mc_name):
    dc_name = ctx.author  # the discord name is the name of the author of the message
    pd.link_dc_ign(mc_name, dc_name)
    """print the result and format it"""
    result = f'```\n' \
             f'discord name: {dc_name}\n' \
             f'minecraft ign: {mc_name}\n' \
             f'```'
    await ctx.send(result)


# write the server status to the channel
@bot.command(name='status', help='check the server status')
@commands.has_any_role('Member', 'Trial Member')
async def status(ctx):
    result = subprocess.run(['mscs', 'status'], stdout=subprocess.PIPE)  # execute mscs status in linux console
    result.stdout.decode('utf-8')
    await ctx.send(result)


@bot.command(name='get_mcname', help='show ign by discord name', pass_context=True)
@commands.has_any_role('Member', 'Trial Member')
async def get_mcname(ctx, dc_name):
    result = 'This command doesn\'t work yet'
    await ctx.send(result)


@bot.command(name='get_dcname', help='show ign by discord name', pass_context=True)
@commands.has_any_role('Member', 'Trial Member')
async def get_dcname(ctx, mc_name):
    result = 'This command doesn\'t work yet'
    await ctx.send(result)


# commands only Owner and Staff can use
# Staff and Owner can send commands via discord chat to the minecraft server
@bot.command(name='command', help='send any command to the server through discord')
@commands.has_any_role('Staff', 'Owner')
# *cmd: the * will make it so that all variables typed in will be stored in the command variable
# if one were to only use cmd as an argument only the first word after the command name would be in the variable
# ig command some mc command -> would be stored in cmd as -> cmd = (some, mc, command)
async def command(ctx, *cmd):
    send_command = ''  # initialize an empty string to add the extra variables in the tuple to
    for i in cmd:  # go over the tuple containing
        send_command += '{} '.format(i)  # add nth value in tuple and a space after id
    send_command = send_command[:-1]  # remove the last space from the cmd
    with open(console_in, 'w') as f:  # open the console.in file to write the commands
        f.writelines('/{}\n'.format(send_command))  # write the command in the console.in file
        f.close()  # close the file


# chat link blocking code
def chat_link():
    tail = FileTail(console_out)  # tail the console.out file
    for line in tail:
        if '[Server thread/INFO]' and '<' and '>' in line:  # check if the message was in fact sent by a player
            if line[33] == '>':
                return line
    return


# chat link async function ran in executor
async def link_async_func():
    await bot.wait_until_ready()  # await until the bot is ready
    send_channel = bot.get_channel(CHAT_LINK_CHANNEL)  # specify the chat link discord channel
    with features.ThreadPoolExecutor() as pool:  # run a thread pool executor
        while True:  # while true -> always
            line = await bot.loop.run_in_executor(pool, chat_link)  # run chat_link in executor
            await send_channel.send(line[33:])  # send the output to chat without timestamp and console msg type


bot.loop.create_task(link_async_func())  # run the loop for the chat link
bot.run(token)  # run the loop for the bot
