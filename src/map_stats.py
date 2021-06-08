#!/usr/bin/env python3

from os.path import join

import pandas as pd


def get_player_map_stats(tournament, match_number, map_number):
    try:
        match_number = int(match_number)
        match_number = 'match_' + str(match_number)
    except ValueError:
        print(f'Match number of {match_number} is invalid')
        exit()

    try:
        map_number = int(map_number)
        map_number = 'map_' + str(map_number)
    except ValueError:
        print(f'Map number of {match_number} is invalid')
        exit()

    dirpath = join('../data', tournament, match_number, map_number)
    try:
        players_df = pd.read_csv(join(dirpath, 'players.csv'))
        map_df = pd.read_csv(join(dirpath, 'map.csv'))
    except FileNotFoundError:
        requested_map = dirpath.split('/')
        print(f'Match does not exist: ')


if __name__ == '__main__':
    tournament = 'CR6_2021_Summer'
    match_number = 1
    map_number = 1
    get_player_map_stats(tournament, match_number, map_number)
