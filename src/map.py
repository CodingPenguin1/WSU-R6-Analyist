#!/usr/bin/env python3

from os import name
import pandas as pd
from team import Team


class Map:
    def __init__(self, filepath):
        self.map_df = pd.read_csv(filepath)

        self.name = self.map_df['map'][0]

        self.team_1 = Team(self.map_df['team 1'][0])
        self.team_2 = Team(self.map_df['team 2'][0])

        self.team_1_score = self.map_df['team 1 score'][0]
        self.team_2_score = self.map_df['team 2 score'][0]

        self.team_1_attack_ban = self.map_df['team 1 attack ban'][0]
        self.team_1_defense_ban = self.map_df['team 1 defense ban'][0]
        self.team_2_attack_ban = self.map_df['team 2 attack ban'][0]
        self.team_2_defense_ban = self.map_df['team 2 defense ban'][0]

    def __str__(self):
        return f'{self.name}\n\
{len(self.name) * "-"}\n\
Team 1: {self.team_1}\n\
Team 2: {self.team_2}\n\
Team 1 Bans: {self.team_1_attack_ban} & {self.team_1_defense_ban}\n\
Team 2 Bans: {self.team_2_attack_ban} & {self.team_2_defense_ban}'


if __name__ == '__main__':
    kafe = Map('../data/2021_summer/match_1/map.csv')
    print(kafe)
