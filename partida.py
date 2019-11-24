# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:04:53 2019

@author: Carlos Moreno Morera
"""

from __future__ import print_function
from enum import Enum
from player import Player

State = Enum('State', 'Creation Ask Vote Guess Final')

class Partida:
    
    def __init__(self):
        """
        Class Constructor.
        
        Returns
        -------
        Constructed Player class.
        
        """
        self.__num_turn = 0
        self.__turn = []
        self.__state = State.Creation
        self.__players = {}
    
    def add_player(self, id):
        if (self.__state == State.Creation and not(id in self.__players)):
            self.__players[id] = Player()
            self.__turn.append(id)
            
    def remove_player(self, id):
        if (id in self.__players):
            del self.__players[id]