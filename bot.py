# external libraries and modules
import os  # import module for directory management
from dotenv import load_dotenv  # load module for usage of a .env file
import subprocess  # import module used to do linux code execution
from discord.ext import commands  # import the commands module from discord.py
import concurrent.futures as futures  # import concurrent.features for the executor for the chat link

# scripts made to be used together with the bot
import scoreboard as sc  # import scoreboard.py
import player_data as pd  # import the script to get player data
import chat_link as cl
import server_data as sd
import help


bot = commands.Bot(command_prefix=('ig ', 'Ig '))  # set the command prefix

load_dotenv()  # load the .env file containing id's that have to be kept secret for security
token = os.getenv('DISCORD_TOKEN')  # get our discord bot token from .env

ugly = ['JeSuisLelijk', 'jesuislelijk']


@bot.event
async def on_ready():
    print('Bot connected!')


# check messages when they're send and answer if something triggers the bot
@bot.event
async def on_message(message):  # run when a message has been send
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
            await message.channel.send('The biggest pimp ever', delete_after=20)  # delete the message after 60 sec

    # if the message contains 69 answer nice
    if '69' in message.content:
        if '<' in message.content:
            """correct for possible emoji's containing 69"""
            pass
        else:
            response = 'Nice'
            await message.channel.send(response, delete_after=20)

    # if the message contains 420 answer Haha Weeeeeeed!
    if '420' in message.content:
        if '<' in message.content:
            """correct for possible emoji's containing 69"""
            pass
        else:
            response = 'Haha Weeeeeeed!'
            await message.channel.send(response, delete_after=20)

    # pay respect when someone types F or f
    if message.content in ('F', 'f'):
        response = 'The Ingenium server pays their respect'
        await message.channel.send(response)

    # respond to oof
    if message.content in ('Oof', 'oof'):
        response = 'Oof you done goofed!'
        await message.channel.send(response, delete_after=10)

    # respond to happy birthday
    if 'happy birthday' in message.content or 'Happy Birthday' in message.content:
        response = 'Ingenium wishes you a happy birthday! ðŸŽˆðŸŽ‰'
        await message.channel.send(response)

    if 'ilmango' in message.content:
        response = 'Mango, Mango, Mango mango mango, Mangooooooooooooooooooooooooooooooooooooooooooo'
        await message.channel.send(response, delete_after=30)

    if 'stop lazy' in message.content:
        response = 'stop being lazy prick'
        await message.channel.send(response, delete_after=35)

    if 'stop lazy' in message.content:
        response = 'stop being lazy prick'
        await message.channel.send(response, delete_after=35)

    # chat link code
    if message.channel.id == sd.CHAT_LINK_CHANNEL:  # only send messages sent in the chat link channel
        # get both the content of the message as well as it's author
        msg = message.content
        sender = message.author
        if not msg.startswith('ig ') and not msg.startswith('Ig '):  # ignore bot commands
            # use the tellraw command to send messages in in game chat & add some colour formatting
            # begin the message with [discord] to show it's a discord message sent the message
            # remove #xxxx from the senders discord tag and put the name in < >
            dc_msg_in_game = 'tellraw @a [{{\"text\":\"[Discord] \", \"color\":\"blue\"}}, {{\"text\":\"<{}> {}\",' \
                    ' \"color\":\"white\"}}]\n'.format(str(sender)[:-5], str(msg))
            # go through all servers and send the message
            for world in sd.servers:
                with open(sd.console_in.format(world), 'w') as f:  # open console file to write the command
                    f.writelines(dc_msg_in_game)
                    f.close()
                    await bot.process_commands(message)

    await bot.process_commands(message)


# when a new player joins, write the welcome message
@bot.event
async def on_member_join(member):
    # mention with .mention, \n will add a newline in the f string
    response = (f'Hi {member}, welcome to the Ingenium Discord server!. \n'
                f'You can find our rules as well as other information about the server in {bot.get_channel(sd.server_rules_and_info).mention}. \n'
                f'If you want to apply, head over to {bot.get_channel(sd.how_to_apply).mention} and follow the instructions. \n'
                f'Let us know where you are from in in {bot.get_channel(sd.server_rules_and_info).mention}. \n'
                f'Feel free to introduce yourself in {bot.get_channel(sd.introduce_yourself).mention}. \n'
                f'You can start talking to us in {bot.get_channel(sd.general_chat).mention}.\n'
                f'\n'
                f'If you have any questions feel free to ask our staff about it! \n'
                f'We hope you will have a pleasant time on the server!')
    await bot.get_channel(sd.welcome).send(response)


# commands everyone can uses
# set different commands the bot will respond to
# name sets the commands name, help will trigger at ig help
@bot.command(name='test', help='test if the bot is working')
async def test_bot(ctx):
    response = 'Don\'t worry, I\'m working!'
    await ctx.send(response)


# display a scoreboard of an objective with the first number amount of players
# if number is not given, then all will be displayed
@bot.command(name='scoreboard', help=help.scoreboard)
async def scoreboard(ctx, objective, number=''):
    result = sc.display(objective, number)  # get result from the scoreboard display function
    if result != 'unknown':
        await ctx.send(result)
    else:
        await ctx.send('```css\n[I\'m sorry but this is not a valid objective.] \n'
                       '[check help playerscore to see a list of valid objectives]\n```')


# command to fetch scoreboard data of a single player and a single scoreboard
@bot.command(name='playerscore', help=help.playerscore)
async def playerscore(ctx, objective, player):
    if player not in pd.players():
        await ctx.send('```css\n[I\'m sorry but this user has not been found.]```')
    data = sc.player(objective, player)
    if data != 'unknown':
        result = f'```{player}: {objective} = {data}```'
        await ctx.send(result)
    else:
        await ctx.send('```css\n[I\'m sorry but this is not a valid objective.] \n'
                       '[check help playerscore to see a list of valid objectives]\n```')


# display the world seed
@bot.command(name='seed', help='Display the server\'s seed')
async def show_seed(ctx):
    result = sd.seed
    await ctx.send(f'`{result}`')


# divide the coords by 8
@bot.command(name='ow2nether', help='Convert overworld coordinates to nether coordinates.')
async def ow2n(ctx, x, z):
    await ctx.send(f'`{x}, {z} -> {round(int(x) / 8)}, {round(int(z) / 8)}`')


# multiply coords by 8
@bot.command(name='nether2ow', help='Convert nether coordinates to overworld coordinates.')
async def n2ow(ctx, x, z):
    await ctx.send(f'`{x}, {z} -> {round(int(x) * 8)}, {round(int(z) * 8)}`')


# commands only Members, Trial members and Friends can use
@bot.command(name='whitelist', help='Show the list of all whitelisted players.')
@commands.has_any_role('Member', 'Trial Member', 'Friends')
async def whitelist(ctx):
    players = sorted(pd.players())
    result = '```'
    for p in players:
        result += p + (20 - len(p)) * ' ' + ' | '
    result += '```'
    await ctx.send(result)


# get th ip of a server
@bot.command(name='ip', help=help.ip)
@commands.has_any_role('Member', 'Trial Member')
async def show_ip(ctx, server):
    if server not in sd.servers:
        await ctx.send('```css\n[This is not a valid server. Check the valid servers in ip help]\n```')
    else:
        result = sd.ips[server]
        await ctx.send(f'`{result}`')


# use the server locations from server_data.py to display the coordinates of a certain location
@bot.command(name='location', help=help.server_location)
@commands.has_any_role('Member', 'Trial Member')
async def location(ctx, *locations):
    place = ''
    for l in locations:
        place += l + ' '
    place = place[:-1]
    place = place.replace('_', ' ')
    if place not in sd.server_locations:
        await ctx.send('```css\n[This is not a valid location. See help locations for more information]\n```')
    else:
        result = sd.server_locations[place.lower()]
        await ctx.send(f'`{place.lower()} nether roof coordinates: {result}`')


# write the server status to the channel
@bot.command(name='status', help=help.status)
@commands.has_any_role('Member', 'Trial Member')
async def status(ctx, server):
    if server not in sd.servers:
        await ctx.send('```css\n[This is not a valid server. Check the valid servers in ip help]\n```')
    else:
        cmd_out = subprocess.run(['mscs', 'status'], stdout=subprocess.PIPE)  # execute mscs status in linux console
        decoded = cmd_out.stdout.decode('utf8')
        info = decoded.split('\n')
        for line in info:  # is server: is in the line
            if server + ':' in line:  # then the status is in that line, so we just write that in chat
                result = '```' + line[2:] + '```'  # add discord code block formatting
                await ctx.send(result)


# show how many players are online and which players are online
@bot.command(name='online', help=help.online)
@commands.has_any_role('Member', 'Trial Member')
async def online(ctx, server):
    if server not in sd.servers:
        await ctx.send('```css\n[This is not a valid server. Check the valid servers in ip help]\n```')
    else:
        cmd_out = subprocess.run(['mscs', 'status'], stdout=subprocess.PIPE)  # execute mscs status in linux console
        # get stdout from CompletedProcess class
        # decode b string to utf8
        decoded = cmd_out.stdout.decode('utf8')
        info = decoded.split('\n')  # split into tuple on \n
        for pos, line in enumerate(info):
            if server + ':' in line:  # if the required server name followed by a colon
                # get the players that are online -> is between ( )
                number = line[line.find('(') + 1:line.find(')')]
                # players that are online are in the next position in the iteration
                players = info[pos + 1][4:]  # remove some redundant spaces
                result = f'```{number}\n'
                result += f'{players}```' if int(number[0]) >= 1 else f'```'
                await ctx.send(result)


# link the minecraft ign to the discord name
# pass_context makes sure we can read info like message sender and more
@bot.command(name='link_name', help='link minecraft ign to discord screen name', pass_context=True)
@commands.has_any_role('Member', 'Trial Member')
async def link_name(ctx, mc_name):
    dc_name = ctx.author  # the discord name is the name of the author of the message
    link = pd.link_dc_ign(mc_name, dc_name)  # write both names in the file where it's stored
    """print the result and format it"""
    # send a message to let people know if it was successful or not
    await ctx.send('```' + link + '```')
    if link == 'Your name has been registered successfully!':
        result = f'```\n' \
             f'discord name: {dc_name}\n' \
             f'minecraft ign: {mc_name}\n' \
             f'```'
        await ctx.send(result)


# display the player info of whitelisted players
@bot.command(name='player_info', help='Get someones player name, discord name and basic server stats.')
@commands.has_any_role('Member', 'Trial Member')
async def player_info(ctx, name):
    dc, mc = pd.info(name)
    if not dc:
        await ctx.send('```css\n[I\'m sorry but this user has not been found.] \n'
                       '[This player either does not exist or has not linked their accounts.]\n```')

    # get play minutes and pick uses stats
    play_minutes = sc.player('play_minutes', mc)
    pick_uses = sc.player('pick_uses', mc)
    # format them in 4 rows, discord name, mc ign, play minutes & pick uses
    result = f'Discord name:   {dc}\n' \
             f'Minecraft ign:  {mc}\n' \
             f'Play minutes:   {play_minutes}\n' \
             f'Blocks mined:   {pick_uses}'
    await ctx.send('```' + result + '```')


# next 2 are analogous to player_info but showing less
# these are only  small utility commands to know who's who in game and on dc
@bot.command(name='get_mcname', help='show ign by discord name')
@commands.has_any_role('Member', 'Trial Member')
async def get_mcname(ctx, dc_name):
    dc, mc = pd.info(dc_name)
    if not dc:  # error message in case of a wrong name
        await ctx.send('```css\n[I\'m sorry but this user has not been found.] \n'
                       '[This player either does not exist or has not linked their accounts.]\n```')
    else:
        await ctx.send(f'```{dc} is {mc} in minecraft```')


@bot.command(name='get_dcname', help='show discord name by ign name')
@commands.has_any_role('Member', 'Trial Member')
async def get_dcname(ctx, mc_name):
    dc, mc = pd.info(mc_name)
    if not dc:  # error message in case of a wrong name
        await ctx.send('```css\n[I\'m sorry but this user has not been found.] \n'
                       '[This player either does not exist or has not linked their accounts.]\n```')
    else:
        await ctx.send(f'```{mc} is {dc} in minecraft```')


@bot.command(name='start', help=help.start)
@commands.has_any_role('Member', 'Trial Member')
async def start(ctx, server):
    if server not in sd.servers:
        await ctx.send('```css\n[This is not a valid server. Check the valid servers in help start]\n```')
    else:
        cmd = subprocess.run(['mscs'] + ['start'] + [server], stdout=subprocess.PIPE)  # start the server
        result = '```' + cmd.stdout.decode('utf8') + '```'
        await ctx.send(result)


# commands only Owner and Staff can use
# Staff and Owner can send commands via discord chat to the minecraft server
@bot.command(name='command', help='send any command to the server through discord')
@commands.has_any_role('Staff', 'Owner')
# *cmd: the * will make it so that all variables typed in will be stored in the command variable
# if one were to only use cmd as an argument only the first word after the command name would be in the variable
# ig command some mc command -> would be stored in cmd as -> cmd = (some, mc, command)
async def command(ctx, server, *cmd):
    if server not in sd.servers:
        await ctx.send('```css\n[This is not a valid server]\n```')
    send_command = ''  # initialize an empty string to add the extra variables in the tuple to
    for i in cmd:  # go over the tuple containing
        send_command += '{} '.format(i)  # add nth value in tuple and a space after id
    send_command = send_command[:-1]  # remove the last space from the cmd
    with open(sd.console_in.format(server), 'w') as f:  # open the console.in file to write the commands
        f.writelines('/{}\n'.format(send_command))  # write the command in the console.in file
        f.close()  # close the file


@bot.command(name='mscs', help=help.mscs)
@commands.has_any_role('Staff', 'Owner')
async def mscs(ctx, *cmd):
    cmd = subprocess.run(['mscs'] + [i for i in cmd], stdout=subprocess.PIPE)  # execute mscs cmd in linux console
    result = '```' + cmd.stdout.decode('utf8') + '```'
    await ctx.send(result)


@bot.command(name='shell_command', help=help.shell)
@commands.has_any_role('Staff', 'Owner')
async def shell_command(ctx, *cmd):
    cmd = subprocess.run([i for i in cmd], stdout=subprocess.PIPE)  # execute command in linux console
    result = '```' + cmd.stdout.decode('utf8') + '```'
    await ctx.send(result)


# chat link async function ran in executor
async def link_async_func(server):
    await bot.wait_until_ready()  # await until the bot is ready
    send_channel = bot.get_channel(sd.CHAT_LINK_CHANNEL)  # specify the chat link discord channel
    with futures.ThreadPoolExecutor() as pool:  # run a thread pool executor
        while True:  # while true -> always
            line = await bot.loop.run_in_executor(pool, cl.chat_link, server)  # run chat_link in executor
            if 'tellraw' not in line:
                await send_channel.send('**[{}]** '.format(server) + line[33:])


# give_ranks.start()
bot.loop.create_task(link_async_func('SMP'))  # run the loop for the SMP link
bot.loop.create_task(link_async_func('CMP'))  # run the loop for the CMP link
bot.loop.create_task(link_async_func('FMP'))  # run the loop for the FMP link
bot.run(token)  # run the loop for the bot
