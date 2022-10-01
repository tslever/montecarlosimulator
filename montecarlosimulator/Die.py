'''
Module for class Die, which may be rolled to select a face
'''

import numpy as np
import pandas as pd

class Die:
    '''
    May be rolled to select a face.
    Has N sides.
    Each side is associated with a face and a weight.

    Instance variables:
        __data_frame_of_faces_and_weights

    Public methods:
        __init__
        change_weight
        roll
        show
    '''

    def __init__(self, array_of_faces):
        '''
        Initializes a Die object
        
        Keyword arguments:
            array_of_faces -- a 1D numpy array of faces. A face must have a data type of string, int, or float. All faces in the numpy array have the same data type. The faces in the numpy array must be unique.

        Return values:
            none

        Side effects:
            Initializes this Die object's data frame of faces and weights

        Exceptions raised:
            none

        Restrictions on when this method can be called:
            May not be called directly
        '''

        array_of_weights = np.ones(len(array_of_faces))
        self.__data_frame_of_faces_and_weights = pd.DataFrame({'weight': array_of_weights}, index = array_of_faces)

    def change_weight(self, face, weight):
        '''
        Changes the weight of a provided face to a provided weight

        Keyword arguments:
            face -- A string, integer, or floating-point number
            weight -- A floating-point number

        Return values:
            none

        Side effects:
            Changes the weight of the provided face to the provided weight

        Exceptions raised:
            ValueError, if the provided face is not in the index of this Die object's dataframe of faces and weights, or if the provided weight cannot be converted to a np.float64 object

        Restrictions on when this method can be called:
            none
        '''

        if face not in self.__data_frame_of_faces_and_weights.index:
            raise ValueError('face is not in index of faces')
        # Checks to see if weight can be converted to np.float64.
        # If not, raises ValueError: could not convert <weight type> to float: <weight value>
        weight = np.float64(weight)
        self.__data_frame_of_faces_and_weights.set_value(face, 'weight', weight)

    def roll(self, number_of_rolls = 1):
        '''
        Rolls this Die object one or more times

        Keyword arguments:
            number_of_rolls -- An integer

        Return values:
            data_frame_of_rolled_faces_and_weights -- A data frame of rolled faces and weights

        Side effects:
            Samples rows from the data frame of faces and weights of this Die object according to the weights.
        
        Exceptions raised:
            none

        Restrictions on when this method can be called:
            none
        '''

        data_frame_of_rolled_faces_and_weights = self.__data_frame_of_faces_and_weights.sample(n = number_of_rolls, replace = True, weights = 'weight', random_state = None, axis = None, ignore_index = False)
        return data_frame_of_rolled_faces_and_weights.index.to_list()

    def show(self):
        '''
        Displays and provides the data frame of faces and weights of this Die object

        Keyword arguments:
            none

        Return values:
            __data_frame_of_faces_and_weights -- The data frame of faces and weights of this Die object

        Side effects:
            Displays the data frame of faces and weights of this Die object

        Exceptions raised:
            none

        Restrictions on when this method can be called:
            none
        '''

        print(self.__data_frame_of_faces_and_weights)
        return self.__data_frame_of_faces_and_weights