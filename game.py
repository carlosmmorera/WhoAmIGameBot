# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:04:53 2019

@author: Carlos Moreno Morera
"""

from __future__ import print_function
from player import Player
import confgame as cfg
import random
import time

class Game:
    """
    Game class implements necessary methods to manage a Who Am I game.
    
    Attributes
    ----------
    __num_turn: int
        Number of the actual turn.
    __turn: list
        List of players identifier which determines next player turn.
    __first_player: int
        Indentifier of the player who started playing this game.
    __state: cfg.State
        State of the game.
    __players: dict
        Dictionary of players in this game.
    __init_time: float
        Initial time of the last votation.
    __question: str
        Question of the last votation.
    __votes: dict
        Dictionary which stores the votation results.
    
    """
    def __init__(self):
        """
        Class Constructor.
        
        Returns
        -------
        Constructed Game class.
        
        """
        self.__num_turn = 0
        self.__turn = []
        self.__first_player = None
        self.__state = cfg.State.Creation
        self.__players = {}
        self.__init_time = None
        self.__question = ""
        self.__votes = {'Yes': 0, 'No': 0}
    
    def add_player(self, id):
        """
        Adds a player to the game.
        
        Returns
        -------
        None.
        
        """
        if (self.__state == cfg.State.Creation and not(id in self.__players)):
            self.__players[id] = Player()
            self.__turn.append(id)
            
    def remove_player(self, id):
        """
        Removes a player from the game.
        
        Returns
        -------
        None.
        
        """
        if (self.__state == cfg.State.Final and id in self.__players):
            del self.__players[id]
            
    def get_num_players(self):
        """
        Gets the number of players in the game.
        
        Returns
        -------
        int: number of players in the game.
        """
        return len(self.__players)
    
    def __set_char(self, writer, recipient, received):
        """
        Sets a character to the recipient player from the writer player.
        
        Parameters
        ----------
        writer: int
            Index in turn list which indicates the identifier of the writer
            player.
        recipient: int
            Index in turn list which indicates the identifier of the recipient
            player.
        received: list
            List of booleans which indicates which player in turn list has
            already received a character.
            
        Returns
        -------
        None.
        """
        self.__players[self.__turn[recipient]].set_a_character(self.__turn[writer])
        received[recipient] = True
        
    def __first_false(self, l):
        """
        Finds the first element false in a list.
        
        Parameters
        ----------
        l: list
            List of booleans.
            
        Returns
        -------
        int: the index of the first false element.
        """
        i = 0
        while (i < len(l) and l[i]):
            i += 1
        return i
    
    def distribute_characters(self):
        """
        Distributes the characters between the players in the game. Each
        player must receive an only character from another different player.
        
        Returns
        -------
        None.
        """
        if self.__state == cfg.State.Distribution:
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
                
                self.__set_char(i, j, received)
                num_given += 1
            
            sec_last = self.get_num_players() - 2
            last = self.get_num_players() - 1
            
            if not(received[sec_last]):
                if received[last]:
                    self.__set_char(last, sec_last, received)
                    self.__set_char(sec_last, self.__first_false(received), received)
                else:
                    self.__set_char(last, sec_last, received)
                    self.__set_char(sec_last, last, received)
            elif not(received[last]):
                self.__set_char(sec_last, last, received)
                self.__set_char(last, self.__first_false(received), received)
            else:
                l = [sec_last, last]
                random.shuffle(l)
                self.__set_char(l[0], self.__first_false(received), received)
                self.__set_char(l[1], self.__first_false(received), received)
                
            self.__state = cfg.State.TurnDetermination
            
    def start_votation(self, q):
        """
        Starts the votation phase.
        
        Returns
        -------
        None.
        """
        if self.__state == cfg.State.Vote:
            self.__votes['Yes'] = 0
            self.__votes['No'] = 0
            self.__question = q
            self.__init_time = time.time()
    
    def vote_yes(self):
        """
        Adds an affirmative vote to the votation in process.
        
        Returns
        -------
        None.
        """
        if self.__state == cfg.State.Vote:
            self.__votes['Yes'] += 1
            
    def vote_no(self):
        """
        Adds an negative vote to the votation in process.
        
        Returns
        -------
        None.
        """
        if self.__state == cfg.State.Vote:
            self.__votes['No'] += 1
            
    def has_votation_finished(self):
        """
        Checks if the votation state has finished.
        
        Returns
        -------
        bool: True if any of these conditions is true:
            - The state of the game is different than 'Vote' state.
            - Every player has voted.
            - The time of the votation has reached the maximum number of
              seconds.
            False in other case.
        """
        if self.__state != cfg.State.Vote:
            return True
        
        t = time.time() - self.__init_time
        numvotes = self.__votes['Yes'] + self.__votes['No']
        return self.get_num_players() == numvotes or t >= cfg.VOTATION_TIME