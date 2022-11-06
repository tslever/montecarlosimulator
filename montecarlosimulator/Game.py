'''
Module for class Game, which plays by rolling one or more times all dice in a list of one or more dice with the same set of faces
'''

import pandas as pd

class Game:
    '''
    Encapsulates a list of one or more dice with the same set of faces and a method to play by rolling one or more times all dice in the list.

    Instance variables:
        _data_frame_of_rolls_and_dice: pd.DataFrame -- a data frame of rolls and dice, where the number of rows and observations is the number of rolls, the number of columns and features is the number of dice, and each cell value is a face rolled

    Public methods:
        __init__
        play
        show
    '''

    def __init__(self, list_of_dice):
        '''
        Initializes a Game object with a list of one or more dice with the same set of faces
        
        Keyword arguments:
            list_of_dice: list -- a list of one or more dice with the same set of faces

        Return values:
            none

        Side effects:
            Initializes this Die object's list of one or more dice with the same set of faces

        Exceptions raised:
            none

        Restrictions on when this method can be called:
            May not be called directly
        '''

        self._list_of_dice = list_of_dice

    def play(self, number_of_rolls):
        '''
        Plays by rolling one or more times all dice in this Game object's list of one or more dice with the same set of faces

        Keyword arguments:
            number_of_rolls: int -- An integer

        Return values:
            none

        Side effects:
            Creates a data frame of rolls and dice, where the number of rows and observations is the number of rolls, the number of columns and features is the number of dice, and each cell value is a face rolled
        
        Exceptions raised:
            none

        Restrictions on when this method can be called:
            none
        '''

        self._data_frame_of_rolls_and_dice = pd.DataFrame()
        self._data_frame_of_rolls_and_dice.index.rename('roll_index', inplace = True)
        for i in range(0, len(self._list_of_dice)):
            die = self._list_of_dice[i]
            self._data_frame_of_rolls_and_dice[i] = die.roll(number_of_rolls)

    def show(self, form):
        if form == 'narrow':
            narrow_data_frame_of_rolls_and_dice = self._data_frame_of_rolls_and_dice.stack()
            narrow_data_frame_of_rolls_and_dice.rename('face', inplace = True)
            narrow_data_frame_of_rolls_and_dice.index.rename(['roll_index', 'die_index'], inplace = True)
            return narrow_data_frame_of_rolls_and_dice
        elif form == 'wide':
            return self._data_frame_of_rolls_and_dice
        else:
            raise ValueError('the form of the data frame of rolls and dice must be either narrow or wide')