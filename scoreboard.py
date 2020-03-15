import json  # import module for json file handling
import player_data  # import uuid_converter.py
import math
import nbt

from server_data import JSON_objectives
from server_data import NBT_objectives
from server_data import objectives_m
from server_data import objectives_km
from server_data import stat_directory


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
    stat = []

    # go through the dictionary and get the uuid and playername
    if datatype == 'JSON':
        # get the dictionary containing the uuid and playernames
        mapped_uuid = player_data.generate(save=False)

        for id, playername in mapped_uuid.items():
            try:
                data = get_json_stat(stat_directory, sub_type, objective, sc, id)
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
