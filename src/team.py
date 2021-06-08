#!/usr/bin/env python3

import pandas as pd


class Team:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
