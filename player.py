# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:55:25 2019

@author: Carlos Moreno Morera
"""
from __future__ import print_function

class Player:
    """
    Player class implements setters and getters of the information needed for
    each game player.
    
    Attributes
    ----------
    __turn: int
        Number of turns played.
    __char: str
        Character written by the player and which will be assigned to another
        player.
    __clarif: str
        Optional clarification of the character written by the player.
    __id_writer: int
        Unique Telegram identifier of the user who wrote the character assigned
        to this player.
        
    """
    def __init__(self):
        """
        Class Constructor.
        
        Returns
        -------
        Constructed Player class.
        
        """
        self.__turn = 0
        self.__char = None
        self.__clarif = None
        self.__id_writer = None
         
    def set_a_character(self, writer):
        """
        Sets the writer whom wrote the secret character of this player
        
        Parameters
        ----------
        writer: int
            Unique Telegram identifier of the user who wrote the character 
            assigned to this player.
            
        Returns
        -------
        None.
        
        """
        self.__id_writer = writer
         
    def save_new_character(self, char, clarif = None):
        """
        Sets the character and its clarification, both were written by this
        player.
        
        Parameters
        ----------
        char: str
            Character written by the player and which will be assigned to another
            player.
        clarif: str (optional)
            Clarification of the character written by the player.
            
        Returns
        -------
        None.
        """
        self.__char = char
        self.__clarif = clarif
         
    def increase_turn(self):
        """
        Increases the player's turn.
        
        Returns
        -------
        None.
        """
        self.__turn += 1
         
    def get_turn(self):
        """
        Gets the player's turn.
        
        Returns
        -------
        int: Player's turn.
        """
        return self.__turn
    
    def has_clarification(self):
        """
        Asks if there is a clarification for the character written by this
        player.
        
        Returns
        -------
        bool: True if there is a clarification and False in other case.
        """
        return self.__clarif is not None
    
    def has_character(self):
        """
        Checks if the player has written its character.
        
        Returns
        -------
        bool: True if there is a character and False in other case.
        """
        return self.__char is not None
    
    def get_character(self):
        """
        Gets the character written by the player.
        
        Returns
        -------
        str: character.
        """
        return self.__char
    
    def get_clarification(self):
        """
        Gets the clarification written by the player.
        
        Returns
        -------
        str: clarification.
        """
        return self.__clarif
    
    def who_gave_me(self):
        """
        Gets the unique Telegram identifier of the player who wrote the
        character which was assigned to this player.
        
        Returns
        -------
        str: player's identifier.
        """
        return self.__id_writer