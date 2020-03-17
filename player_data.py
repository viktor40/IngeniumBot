import urllib
from urllib.request import urlopen
import json
import re
import numpy as np
import time

from server_data import whitelist


# generate a dictionary mapping the uuid's to the playernames
def generate(save=False):
    with open(whitelist) as f:  # open the json file containing the whitelist
        data = json.load(f)

    # map the uuid to the igk
    player_info = {player['uuid']: player['name'] for player in data}
    array = np.array(list(player_info.items()))  # array wil look like [[uuid, name], [uuid, name] ... ]
    np.savetxt('players.txt', X=array, fmt='%s') if save else None
    f.close()
    return player_info


# access the mojang api to convert missing uuid's to player names
def make_playername(UUID_file, save=False):
    link = 'https://sessionserver.mojang.com/session/minecraft/profile/{}'
    with open(UUID_file, 'r') as f:
        UUIDs = f.readlines()

    igns, dict_igns = [], {}
    for id in UUIDs:
        try:
            request = link.format(re.sub('-', '', id.strip()))
            response = json.loads(urlopen(request).read())
            playername = response['name']
            igns.append(playername)
            dict_igns[id.strip()] = playername

        except urllib.error.HTTPError:
            time.sleep(2)
            request = link.format(re.sub('-', '', id.strip()))
            response = json.loads(urlopen(request).read())
            playername = response['name']
            igns.append(playername)
            dict_igns[id.strip()] = playername

        except json.decoder.JSONDecodeError:
            pass

    array = np.array(list(dict_igns.items()))
    np.savetxt('players.txt', X=array, fmt='%s') if save else None
    f.close()
    return dict_igns


# convert a file with 2 columns of data to a dictionary
def from_file(file):
    data = np.loadtxt(file, dtype='str')
    return {row[0]: row[1] for row in data}


# get a list only containing player names
# analogous to the generate function
def players(save=False):
    with open(whitelist) as f:
        data = json.load(f)

    player = [player['name'] for player in data]
    np.savetxt('players_only.txt', X=player, fmt='%s') if save else None
    f.close()
    return player


# link the discord name to the ign
def link_dc_ign(mc_name, dc_name):
    datafile = 'dc_to_ign.txt'  # specify the output datafile
    # load the datafile adn ignore #xxxx after discord name by setting comment character in file to %
    players_whitelisted = players()
    if mc_name not in players_whitelisted:
        return 'This account is not whitelisted.'
    file_content = np.loadtxt(datafile, dtype='str', comments='%')
    # check if the user didn't already linked the mc username with his discord name
    for member in file_content:
        if member[0] == str(dc_name):  # return if author already linked the names
            return 'Your name is already registered!'
    # append the names to the ndarray along the 0th axis
    file_content = np.append(file_content, [[dc_name, mc_name]], axis=0)
    np.savetxt(datafile, X=file_content, fmt='%s')  # write the new array to the file
    return 'Your name has been registered successfully!'


# dc name from mc name or mc name from dc name
def info(name):
    data = np.loadtxt('dc_to_ign.txt', dtype='str', comments='%')
    for dc, mc in data:
        if name == dc or name == mc or name == dc[:-5]:
            return dc, mc
    return False, False
