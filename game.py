# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:04:53 2019

@author: Carlos Moreno Morera
"""

from __future__ import print_function
from enum import Enum
from player import Player
import random

State = Enum('State', 'Creation Ask Vote Guess Final')

class Game:
    
    def __init__(self):
        """
        Class Constructor.
        
        Returns
        -------
        Constructed Game class.
        
        """
        self.__num_turn = 0
        self.__turn = []
        self.__state = State.Creation
        self.__players = {}
    
    def add_player(self, id):
        """
        Adds a player to the game.
        
        Returns
        -------
        None.
        
        """
        if (self.__state == State.Creation and not(id in self.__players)):
            self.__players[id] = Player()
            self.__turn.append(id)
            
    def remove_player(self, id):
        """
        Removes a player from the game.
        
        Returns
        -------
        None.
        
        """
        if (id in self.__players):
            del self.__players[id]
            
    def get_num_players(self):
        """
        Gets the number of players in the game.
        
        Returns
        -------
        int: number of players in the game.
        """
        return len(self.__players)
    
    def distribute_characters(self):
        received = [False for i in range(self.get_num_players())]
        num_given = 0
        
        for i in range(self.get_num_players() - 2):
            shift = random.randint(1, self.get_num_players() - num_given - 1)
            j = i
            
            while (shift > 0):
                if j < self.get_num_players() - 1:
                    j += 1
                else:
                    j = 0
                
                if not(received[j]) and j != i:
                    shift -= 1
                    
            self.__players[self.__turn[j]].set_a_character(self.__turn[i])
            num_given += 1
            received[j] = True
            
        #No terminada, falta repartir a los últimos dos jugadores
            