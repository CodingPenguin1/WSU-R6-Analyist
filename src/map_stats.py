#!/usr/bin/env python3

from os.path import join

import pandas as pd


def get_player_map_stats(tournament, match_number, map_number, player_name):
    # Parameter validation
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
        print(f'Match does not exist: {tournament} | match {match_number} | map {map_number}')
        exit()

    # Filter dataframe to just stats of player_name
    player_df = players_df.loc[players_df['player'] == player_name]

    # Stats
    stats = {}
    stats['kills'] = player_df['kills'].sum()
    stats['deaths'] = player_df['deaths'].sum()
    stats['trades'] = player_df['trade'].sum()
    stats['objectives'] = player_df['objective'].sum()
    stats['rounds'] = len(player_df)
    stats['k/d'] = stats['kills'] / stats['deaths']
    stats['kpr'] = stats['kills'] / stats['rounds']
    print(stats)


if __name__ == '__main__':
    tournament = 'CR6_2021_Summer'
    match_number = 1
    map_number = 1
    player = 'CodingPenguin1'
    get_player_map_stats(tournament, match_number, map_number, player)
