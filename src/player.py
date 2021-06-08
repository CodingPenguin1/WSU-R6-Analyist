#!/usr/bin/env python3

import pandas as pd


class Player:
    def __init__(self, df, name):
        self.name = name
        self.df = df.loc[df['player'] == name]

        self.team = self._get_team()

    def _get_team(self):
        print(self.df)


if __name__ == '__main__':
    players_df = pd.read_csv('../data/2021_summer/match_1/players.csv')
    penguin = Player(players_df, 'CodingPenguin1')
