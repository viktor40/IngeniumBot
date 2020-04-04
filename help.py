# scoreboard command
scoreboard = f'Print the scoreboard you want to get to the chat.\n' \
             f'The first word after the command is the name of the scoreboard.\n' \
             f'The second thing can be either nothing, which displays the complete scoreboard. ' \
             f'If it\'s a number, then only the first [number] of people on the scoreboard will be displayed. ' \
             f'If it\'s all, all players will be on the scoreboard.\n' \
             f'The names of the scoreboards that are implemented are:\n' \
             f'\n' \
             f'-----general-----\n' \
             f'play_minutes, time_since_death_minutes, time_since_death_hours, open_shulker, mobs_killed, traded, ' \
             f'distance_flown_m, distance_walked_m, distance_flown_km, distance_walked_km\n' \
             f'\n' \
             f'-----used-----\n' \
             f'pick_uses, axe_uses, hoe_uses, shovel_uses, sponges_placed, slime_placed, stone_placed, grass_placed, ' \
             f'rails_placed\n' \
             f'\n' \
             f'-----crafted-----\n' \
             f'redstone_torches_crafted, repeaters_crafted, pistons_crafted, comparators_crafted, observers_crafted, ' \
             f'droppers_crafted\n' \
             f'\n' \
             f'-----mined-----\n' \
             f'quartz_mined, diamonds_mined, obsidian_mined\n' \
             f'\n' \
             f'-----custom-----\n' \
             f'slime_peri, witch_peri'

playerscore = f'Print the score in a scoreboard of a certain player.\n' \
              f'The first word after the command is the name of the scoreboard.\n' \
              f'The second word is the ign of the player of whom you want to see the score.\n' \
              f'The names of the scoreboards that are implemented are:\n' \
              f'\n' \
              f'-----general-----\n' \
              f'play_minutes, time_since_death_minutes, time_since_death_hours, open_shulker, mobs_killed, ' \
              f'traded, distance_flown_m, distance_walked_m, distance_flown_km, distance_walked_km\n' \
              f'\n' \
              f'-----used-----\n' \
              f'pick_uses, axe_uses, hoe_uses, shovel_uses, sponges_placed, slime_placed, stone_placed, ' \
              f'grass_placed, rails_placed\n' \
              f'\n' \
              f'-----crafted-----\n' \
              f'redstone_torches_crafted, repeaters_crafted, pistons_crafted, comparators_crafted, ' \
              f'observers_crafted, droppers_crafted\n' \
              f'\n' \
              f'-----mined-----\n' \
              f'quartz_mined, diamonds_mined, obsidian_mined\n' \
              f'\n' \
              f'-----custom-----\n' \
              f'slime_peri, witch_peri'

ip = f'Get the ip of the server. \n' \
     f'The different possibilities are:\n' \
     f'survival -> get the SMP ip.\n' \
     f'creative -> get the creative copy ip.\n' \
     f'flatworld -> get the flatworld testingserver ip.\n' \
     f'flatworld2 -> get the alternate flatworld ip (the sandstone flatworld).\n' \
     f'test -> get the ip of the server where we test things like updates etc.'

server_location = f'Get the coordinates of important locations.\n' \
                  f'The coordinates are always to portals on the nether roof.\n' \
                  f'Locations can by either typed in with a space between words or an _.\n' \
                  f'The available locations are:\n' \
                  f'\n' \
                  f'-----General-----\n' \
                  f'spawn, end portal, vindicate, community island, halloween district\n' \
                  f'\n' \
                  f'-----Farms-----\n' \
                  f'ghast farm, gold farm, sand farm old, sand farm new, gravel farm, witch farm, flower farm, ' \
                  f'slime farm, wither killer\n' \
                  f'\n' \
                  f'-----Mining locations-----\n' \
                  f'gravel mining 1, gravel mining 2, gravel mining 3, gravel mining 4, mining mesa, mesa quarry\n' \
                  f'\n' \
                  f'-----Diamond mine locations-----\n' \
                  f'diamond mining north entrance, diamond mining south entrance, diamond mining north end portal, ' \
                  f'diamond mining south end portal'

status = f'Check the server status.\n' \
         f'The command will output the server status, the server version and the number of players online.\n' \
         f'You can either use survival, creative or flatworld to see the status of the different servers.'

online = f'See which players are online.\n' \
          f'The command will output the number of players online as well as which players are online.\n' \
          f'This command won\'t work if the server is offline (see server status command).\n' \
          f'You can either use survival, creative or flatworld to see the status of the different servers.'

mscs = f'Execute any mscs command on the server itself. \n' \
       f'Commands that are possible will be listed but not all of them will be listed.\n' \
       f'It\'s a good idea to only use commands listed in here as others can be a bit trickier.\n' \
       f'The commands that can be used are:\n' \
       f'status, restart [server], start [server], stop [server], ls, force-stop [server], force-start [server]\n' \
       f'All commands should be self explanatory, except for ls. ls will list the worlds that are on the server. \n' \
       f'This command is only accessible to members with the role Staff or Owner.'

shell = f'Only use this when you know what you\'re doing.\n' \
        f'This command allows you to run any shell command onto the server and get it\'s result.\n' \
        f'Although in general, you shouldn\'t use this.'

start = f'Restart the server if it has crashed.\n' \
        f'available servers to restart are: survival, creative and flatworld.'
