# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:47:22 2019

@author: Carlos Moreno Morera
"""
from enum import Enum

State = Enum('State', 'Creation Distribution TurnDetermination Ask Vote Guess Final')

# Minimum number of players needed to start a game.
MIN_NUM_PLAYERS = 2
# Duration (in seconds) of a votation
VOTATION_TIME = 60