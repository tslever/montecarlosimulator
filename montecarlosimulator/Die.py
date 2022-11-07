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
    Weights default to 1.0 and can be changed.

    Class variables:
        _roll_is_being_tested: bool -- an indicator of whether roll is being tested

    Instance variables:
        _data_frame_of_faces_and_weights: pd.DataFrame -- a data frame with an index of faces and a column of weights. A face has a data type of str, int, or float. All faces in the index have the same data type. The faces must be unique. A weight has a data type of float.

    Public methods:
        __init__
        change_weight
        roll
        show
    '''

    _roll_is_being_tested = False

    def __init__(self, array_of_faces):
        '''
        Initializes a Die object
        
        Keyword arguments:
            array_of_faces: np.ndarray -- a 1D numpy array of faces. A face must have a data type of str, int, or float. All faces in the numpy array have the same data type. The faces in the numpy array must be unique.

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
        self._data_frame_of_faces_and_weights = pd.DataFrame({'weight': array_of_weights}, index = array_of_faces)
        if (len(array_of_faces) > 0):
            face = array_of_faces[0]
            self._type_of_face = type(face)
        else:
            self._type_of_face = None

    def change_weight(self, face, weight):
        '''
        Changes the weight of a provided face to a provided weight

        Keyword arguments:
            face: str, int, np.float64 -- A string, integer, or floating-point number
            weight: np.float64 -- A numpy floating-point number

        Return values:
            none

        Side effects:
            Changes the weight of the provided face to the provided weight

        Exceptions raised:
            ValueError, if the provided face is not in the index of this Die object's dataframe of faces and weights, or if the provided weight cannot be converted to a np.float64 object

        Restrictions on when this method can be called:
            none
        '''

        if face not in self._data_frame_of_faces_and_weights.index:
            raise ValueError('face is not in index of faces')
        # Checks to see if weight can be converted to np.float64.
        # If not, raises ValueError: could not convert <weight type> to float: <weight value>
        weight = np.float64(weight)
        self._data_frame_of_faces_and_weights.at[face, 'weight'] = weight

    def roll(self, number_of_rolls = 1):
        '''
        Rolls this Die object one or more times

        Keyword arguments:
            number_of_rolls: int -- An integer

        Return values:
            list_of_rolled_faces: list -- A list of rolled faces

        Side effects:
            Samples rows from the data frame of faces and weights of this Die object according to the weights
        
        Exceptions raised:
            none

        Restrictions on when this method can be called:
            none
        '''
        
        the_random_state = 0 if Die._roll_is_being_tested else None
        data_frame_of_rolled_faces_and_weights = self._data_frame_of_faces_and_weights.sample(n = number_of_rolls, replace = True, weights = 'weight', random_state = the_random_state, axis = None, ignore_index = False)
        list_of_rolled_faces = data_frame_of_rolled_faces_and_weights.index.to_list()
        return list_of_rolled_faces

    def show(self):
        '''
        Displays and provides the data frame of faces and weights of this Die object

        Keyword arguments:
            none

        Return values:
            _data_frame_of_faces_and_weights: pd.DataFrame -- The data frame of faces and weights of this Die object

        Side effects:
            Displays the data frame of faces and weights of this Die object

        Exceptions raised:
            none

        Restrictions on when this method can be called:
            none
        '''

        #print(self._data_frame_of_faces_and_weights)
        return self._data_frame_of_faces_and_weights

    def get_type_of_face(self):
        '''
        Returns the type of a face of this die

        Keyword arguments:
            none

        Return values:
            _type_of_face: numpy.dtype -- The type of a face of this die

        Side effects:
            none

        Restrictions on when this method can be called:
            none
        '''

        return self._type_of_face