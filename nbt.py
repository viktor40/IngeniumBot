import nbtlib  # import module for nbt database handling
import time  # inport time module for performance testing
import player_data  # import uuid_converter.py

from server_data import scoreboard_path


def get_score(objective):
    nbt_file = nbtlib.load(scoreboard_path)  # load the nbt data
    root = nbt_file.root['data']['PlayerScores']  # get to the correct branch: data -> playerscores
    scoreboard = []  # create empty list to store data

    for i in root:
        if i['Objective'] == objective:  # filter on a certain objective
            name = i['Name']  # get player name
            scoreboard.append([name, i['Score']])  # add list containing name & score to scoreboard
    return scoreboard


def get_single_scpore(objective, player):
    nbt_file = nbtlib.load(scoreboard_path)  # load the nbt data
    root = nbt_file.root['data']['PlayerScores']  # get to the correct branch: data -> playerscores
    white_players = player_data.players('whitelist.json')  # load a list of all whitelisted playes from uuid
    if player not in white_players:  # check if player is whitelisted, if not break the operation
        return
    for i in root:
        # print(i)
        if i['Objective'] == objective:  # filter on a certain objective
            name = i['Name']
            if name == player:  # search for the required player
                return i['Score']  # return the score
