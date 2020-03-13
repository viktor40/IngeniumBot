import json  # import module for json file handling
import player_data  # import uuid_converter.py
import math
import nbt
import time

# map the commands to the  JSON file stat.json containing the built in scoreboards
JSON_objectives = {'play_minutes': ('minecraft:play_one_minute', 'minecraft:custom'),
                   'deaths': ('minecraft:deaths', 'minecraft:custom'),
                   'time_since_death_minutes': ('minecraft:time_since_death', 'minecraft:custom'),
                   'time_since_death_hours': ('minecraft:time_since_death', 'minecraft:custom'),
                   'open_shulker': ('minecraft:open_shulker_box', 'minecraft:custom'),
                   'mobs_killed': ('minecraft:mob_kills', 'minecraft:custom'),
                   'traded': ('minecraft:traded_with_villager', 'minecraft:custom'),
                   'distance_flown_m': ('minecraft:fly_one_cm', 'minecraft:custom'),
                   'distance_walked_m': ('minecraft:fly_one_cm', 'minecraft:custom'),
                   'distance_flown_km': ('minecraft:fly_one_cm', 'minecraft:custom'),
                   'distance_walked_km': ('minecraft:fly_one_cm', 'minecraft:custom'),

                   'pick_uses': ('minecraft:diamond_pickaxe', 'minecraft:used'),
                   'hoe_uses': ('minecraft:diamond_hoe', 'minecraft:used'),
                   'axe_uses': ('minecraft:diamond_axe', 'minecraft:used'),
                   'shovel_uses': ('minecraft:diamond_shovel', 'minecraft:used'),
                   'sponges_placed': ('minecraft:sponge', 'minecraft:used'),
                   'slime_placed': ('minecraft:slime_block', 'minecraft:used'),
                   'stone_placed': ('minecraft:stone', 'minecraft:used'),
                   'grass_placed': ('minecraft:grass_block', 'minecraft:used'),
                   'rails_placed': ('minecraft:rail', 'minecraft:used'),

                   'redstone_torches_crafted': ('minecraft:redstone_torch', 'minecraft:crafted'),
                   'repeaters_crafted': ('minecraft:repeater', 'minecraft:crafted'),
                   'pistons_crafted': ('minecraft:piston', 'minecraft:crafted'),
                   'comparators_crafted': ('minecraft:comparator', 'minecraft:crafted'),
                   'observers_crafted': ('minecraft:observer', 'minecraft:crafted'),
                   'droppers_crafted': ('minecraft:dropper', 'minecraft:crafted'),

                   'quartz_mined': ('minecraft:nether_quartz_ore', 'minecraft:mined'),
                   'diamonds_mined': ('minecraft:diamond_ore', 'minecraft:mined'),
                   'obsidian_mined': ('minecraft:obsidian', 'minecraft:mined')}

# map the commands to the NBT file scoreboard.dat containing the custom scoreboards
NBT_objectives = {'slime_peri': 'BlocksMinedPeri',
                  'witch_peri': 'PeriBlocksMined'}

objectives_m = ['distance_flown_m', 'distance_walked_m']
objectives_km = ['distance_flown_km', 'distance_walked_km']


# generate a string formatted to display a scoreboard
def check_type(objective):
    # get the correct id of the objective
    if objective in JSON_objectives:
        """if the scoreboard is a built in one, convert input to correct scoreboard name"""
        data = JSON_objectives[objective]
        datatype = 'JSON'
        objective, sub_type = data[0], data[1]
        return objective, sub_type, datatype

    elif objective in NBT_objectives:
        objective = NBT_objectives[objective]
        datatype, sub_type = 'NBT', None
        return objective, sub_type, datatype
    else:
        return


def get_json_stat(directory, sub_type, objective, sc, id):
    # open the stat file corresponding to the uuid in the directory
    with open(f'{directory}/{id}.json') as f:
        # load the JSON file
        data = json.load(f)
        # get to the right branch in the JSON tree
    data = data.get('stats').get(sub_type)[objective]

    # do some value conversions
    if sc == 'play_minutes':
        data = math.floor(int(data) / (20 * 60))
    elif sc in objectives_m:
        data = math.floor(int(data) / 100)
    elif sc in objectives_km:
        data = math.floor(int(data) / 100000)
    elif sc == 'time_since_death_minutes':
        data = math.floor((int(data) / (20 * 60)))
    elif sc == 'time_since_death_hours':
        data = math.floor(int(data) / (20 * 3600))
    f.close()
    return data


def display(sc, n):
    if n in ('all', ''):  # if we want all the values, set a high enough value as to get all the stats
        n = 100000
    elif int(n) <= 0:  # if the amount of players required is smaller or equal than 0 do nothing and stop the command
        return

    # fetch the info about the objective required to get
    objective, sub_type, datatype = check_type(sc)

    # set the directory of the stat files
    directory = '../mscs/worlds/survival/survival/stats'
    stat = []

    # go through the dictionary and get the uuid and playername
    if datatype == 'JSON':
        # get the dictionary containing the uuid and playernames

        mapped_uuid = player_data.generate(save=False)

        for id, playername in mapped_uuid.items():
            try:
                data = get_json_stat(directory, sub_type, objective, sc, id)

                if int(data) > 0:
                    # add to the list containing the playername and score
                    stat.append((playername, data))

            except FileNotFoundError:  # if the file is not found, do nothing
                pass

            except KeyError:  # if the player does not have a statistic for the objective
                pass

            except TypeError:  # if the player has value None for the objective
                pass

    # if it's a custom command load the values from the NBT data by use of the NBT module
    elif datatype == 'NBT':
        data = nbt.get_score(objective)
        for i in data:
            if i[1] == 0:
                return
            else:
                stat.append(tuple(i))

    else:  # return nothing if the command is unknown
        return

    # sort the stat list from low to high and reverse the list
    stat_sorted = sorted(stat, key=lambda tup: tup[1])[::-1]
    output = '```\n'  # start string with code block formatting
    output += '-----{}-----\n'.format(sc)  # add a title to the list

    # enumerate over the data. We enumerate so we keep track of the number of values in the list
    for i, stat_data in enumerate(stat_sorted):
        # output formatted as: playername + some amount of spaces so the amount of characters between the left
        # side and the number of the stat is always the same + the value
        output += '{}: {} {}\n'.format(stat_data[0].strip('"'), (20 - len(stat_data[0]))*' ', stat_data[1])
        if i + 1 == int(n):  # if the amount of players needed has been reached, i + 1 since i starts from 0
            output += '```'  # end the code block
            return output  # return th output

    output += '```'  # end the code block
    return output  # return if all players have been iterated over


def player(sc, ign):
    # fetch the info about the objective required to get
    objective, sub_type, datatype = check_type(sc)
    directory = 'stats'

    players = player_data.generate()

    for uuid, name in players.items():
        if ign == name:
            id = uuid

    if datatype == 'JSON':
        try:
            data = get_json_stat(directory, sub_type, objective, sc, id)
            return f'```{ign}: {sc} = {data}```'

        except FileNotFoundError:  # if the file is not found, do nothing
            pass

        except KeyError:  # if the player does not have a statistic for the objective
            pass

        except TypeError:  # if the player has value None for the objective
            pass

    # if it's a custom command load the values from the NBT data by use of the NBT module
    elif datatype == 'NBT':
        data = nbt.get_single_scpore(objective, ign)
        return f'```{ign}: {sc} = {data}```'

    else:  # return nothing if the command is unknown
        return
