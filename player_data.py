import urllib
from urllib.request import urlopen
import json
import re
import numpy as np
import time


# generate a dictionary mapping the uuid's to the playernames
def generate(whitelist, save=False):
    with open(whitelist) as f:
        data = json.load(f)

    player_info = {player['uuid']: player['name'] for player in data}
    array = np.array(list(player_info.items()))
    np.savetxt('players.txt', X=array, fmt='%s') if save else None
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
    return dict_igns


# convert the file to a dictionarry
def from_file(file):
    a = np.loadtxt(file, dtype='str')
    dicty = {}

    for regel in a:
        dicty[regel[0]] = regel[1]
    return dicty


def players(whitelist, save=False):
    with open(whitelist) as f:
        data = json.load(f)

    player = [player['name'] for player in data]
    np.savetxt('players_only.txt', X=player, fmt='%s') if save else None
    return player

