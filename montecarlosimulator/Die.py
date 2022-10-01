import numpy as np
import pandas as pd

class Die:
    '''
    May be rolled to select a face.
    Has N sides.
    Each side is associated with a face and a weight.
    '''

    #__data_frame_of_faces_and_weights = pd.DataFrame({'weight': []}, index = [])

    def __init__(self, array_of_faces):
        '''
        Initializes a Die object.
        Takes a numpy array of faces as an argument.
        A face must have a data type of string, int, or float.
        All faces in the numpy array must have the same data type.
        The faces in the numpy array must be unique.
        '''

        array_of_weights = np.ones(len(array_of_faces))
        self.__data_frame_of_faces_and_weights = pd.DataFrame({'weight': array_of_weights}, index = array_of_faces)

    def change_weight(self, face, weight):
        '''
        Changes the weight of a face to a provided weight.
        Takes a face for which to change a weight and a weight to which to change.
        '''

        if face not in self.__data_frame_of_faces_and_weights.index:
            raise ValueError('face is not in index of faces')
        # Checks to see if weight can be converted to np.float64.
        # If not, raises ValueError: could not convert <weight type> to float: <weight value>
        weight = np.float64(weight)
        self.__data_frame_of_faces_and_weights.set_value(face, 'weight', weight)

    def roll(self, rolls = 1):
        '''
        Rolls this Die object one or more times.
        Takes the number of rolls.
        Samples rows from the data frame of faces and weights of this Die object according to the weights.
        Returns a list rolled faces.
        '''

        data_frame_of_rolled_faces_and_weights = self.__data_frame_of_faces_and_weights.sample(n = rolls, replace = True, weights = 'weight', random_state = None, axis = None, ignore_index = False)
        return data_frame_of_rolled_faces_and_weights.index.to_list()

    def show(self):
        '''
        Provides the data frame of faces and weights of this Die object.
        '''

        print(self.__data_frame_of_faces_and_weights)
        return self.__data_frame_of_faces_and_weights