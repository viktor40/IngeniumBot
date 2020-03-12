import nbtlib  # import module for nbt database handling
import time  # inport time module for performance testing
import player_data  # import uuid_converter.py


def get_score(objective):
    nbt_file = nbtlib.load('scoreboard.dat')  # load the nbt data
    root = nbt_file.root['data']['PlayerScores']  # get to the correct branch: data -> playerscores
    white_players = player_data.players('whitelist.json')  # load a list of all whitelisted playes from uuid
    scoreboard = []  # create empty list to store data

    for i in root:
        if i['Objective'] == objective:  # filter on a certain objective
            name = i['Name']  # get player name
            if name in white_players:  # check if player is whitelisted
                scoreboard.append([name, i['Score']])  # add list containing name & score to scoreboard
    return scoreboard
