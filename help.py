# scoreboard command
scoreboard_help = f'Print the scoreboard you want to get to the chat.\n' \
                  f'The first word after the command is the name of the scoreboard.\n' \
                  f'The second thing can be either nothing, which displays the complete scoreboard. ' \
                  f'If it\'s a number, then only the first [number] of people on the scoreboard will be displayed. ' \
                  f'If it\'s all, all players will be on the scoreboard.\n' \
                  f'The names of the scoreboards that are implemented are:\n' \
                  f'\n' \
                  f'-----general-----\n' \
                  f'play_minutes, ' \
                  f'time_since_death_minutes, ' \
                  f'time_since_death_hours, ' \
                  f'open_shulker, ' \
                  f'mobs_killed, ' \
                  f'traded, ' \
                  f'distance_flown_m, ' \
                  f'distance_walked_m, ' \
                  f'distance_flown_km, ' \
                  f'distance_walked_km\n' \
                  f'\n' \
                  f'-----used-----\n' \
                  f'pick_uses, ' \
                  f'axe_uses, ' \
                  f'hoe_uses, ' \
                  f'shovel_uses, ' \
                  f'sponges_placed, ' \
                  f'slime_placed, ' \
                  f'stone_placed, ' \
                  f'grass_placed, ' \
                  f'rails_placed\n' \
                  f'\n' \
                  f'-----crafted-----\n' \
                  f'redstone_torches_crafted, ' \
                  f'repeaters_crafted, ' \
                  f'pistons_crafted, ' \
                  f'comparators_crafted, ' \
                  f'observers_crafted, ' \
                  f'droppers_crafted\n' \
                  f'\n' \
                  f'-----mined-----\n' \
                  f'quartz_mined, ' \
                  f'diamonds_mined, ' \
                  f'obsidian_mined\n' \
                  f'\n' \
                  f'-----custom-----\n' \
                  f'slime_peri, ' \
                  f'witch_peri'

playerscore_help = f'Print the score in a scoreboard of a certain player.\n' \
                   f'The first word after the command is the name of the scoreboard.\n' \
                   f'The second word is the ign of the player of whom you want to see the score.\n' \
                   f'The names of the scoreboards that are implemented are:\n' \
                   f'\n' \
                   f'-----general-----\n' \
                   f'play_minutes, ' \
                   f'time_since_death_minutes, ' \
                   f'time_since_death_hours, ' \
                   f'open_shulker, ' \
                   f'mobs_killed, ' \
                   f'traded, ' \
                   f'distance_flown_m, ' \
                   f'distance_walked_m, ' \
                   f'distance_flown_km, ' \
                   f'distance_walked_km\n' \
                   f'\n' \
                   f'-----used-----\n' \
                   f'pick_uses, ' \
                   f'axe_uses, ' \
                   f'hoe_uses, ' \
                   f'shovel_uses, ' \
                   f'sponges_placed, ' \
                   f'slime_placed, ' \
                   f'stone_placed, ' \
                   f'grass_placed, ' \
                   f'rails_placed\n' \
                   f'\n' \
                   f'-----crafted-----\n' \
                   f'redstone_torches_crafted, ' \
                   f'repeaters_crafted, ' \
                   f'pistons_crafted, ' \
                   f'comparators_crafted, ' \
                   f'observers_crafted, ' \
                   f'droppers_crafted\n' \
                  f'\n' \
                  f'-----mined-----\n' \
                  f'quartz_mined, ' \
                  f'diamonds_mined, ' \
                  f'obsidian_mined\n' \
                  f'\n' \
                  f'-----custom-----\n' \
                  f'slime_peri, ' \
                  f'witch_peri'

ip_help = f'Get the ip of the server. \n' \
          f'The different possibilities are:\n' \
          f'survival -> get the SMP ip.\n' \
          f'creative -> get the creative copy ip.\n' \
          f'flatworld -> get the flatworld testingserver ip.\n' \
          f'flatworld2 -> get the alternate flatworld ip (the sandstone flatworld).\n' \
          f'test -> get the ip of the server where we test things like updates etc.'

server_location_help = f'Get the coordinates of important locations.\n' \
                       f'The coordinates are always to portals on the nether roof.\n' \
                       f'Locations can by either typed in with a space between words or an _.\n' \
                       f'The available locations are:\n' \
                       f'\n' \
                       f'-----General-----\n' \
                       f'spawn, ' \
                       f'end portal, ' \
                       f'vindicate, ' \
                       f'community island, ' \
                       f'halloween district\n' \
                       f'\n' \
                       f'-----Farms-----\n' \
                       f'ghast farm, ' \
                       f'gold farm, ' \
                       f'sand farm old, ' \
                       f'sand farm new, ' \
                       f'gravel farm, ' \
                       f'witch farm, ' \
                       f'flower farm, ' \
                       f'slime farm, ' \
                       f'wither killer\n' \
                       f'\n' \
                       f'-----Mining locations-----\n' \
                       f'gravel mining 1, ' \
                       f'gravel mining 2, ' \
                       f'gravel mining 3, ' \
                       f'gravel mining 4, ' \
                       f'mining mesa, ' \
                       f'mesa quarry\n' \
                       f'\n' \
                       f'-----Diamond mine locations-----\n' \
                       f'diamond mining north entrance, ' \
                       f'diamond mining south entrance, ' \
                       f'diamond mining north end portal, ' \
                       f'diamond mining south end portal'

status_help = f'Check the server status.\n' \
              f'The command will output the server status, the server version and the number of players online.\n' \
              f'You can either use survival, creative or flatworld to see the status of the different servers.'

players_help = f'See which players are online.\n' \
               f'The command will output the number of players online as well as which players are online.\n' \
               f'This command won\'t work if the server is offline (see server status command).\n' \
               f'You can either use survival, creative or flatworld to see the status of the different servers.'

mscs_help = f'Execute any mscs command on the server itself. \n' \
            f'Commands that are possible will be listed but not all of them will be listed.\n' \
            f'It\'s a good idea to only use commands listed in here as others can be a bit trickier.\n' \
            f'The commands that can be used are:\n' \
            f'status, restart [server], start [server], stop [server], ls, force-stop [server], force-start [server]\n' \
            f'All commands should be self explanatory, except for ls. ls will list the worlds that are on the server. \n' \
            f'This command is only accessible to members with the role Staff or Owner.'

shell_help = f'Only use this when you know what you\'re doing.\n' \
             f'This command allows you to run any shell command onto the server and get it\'s result.\n' \
             f'Although in general, you shouldn\'t use this.'
