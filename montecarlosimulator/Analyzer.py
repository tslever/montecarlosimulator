'''
Module for class Analyzer, which generates structures of descriptive statistics for a game that has been played
'''

class Analyzer:
    '''
    Encapsulates structures of descriptive statistics for a game that has been played and methods to generate these structures of descriptive statistics

    Instance variables:
        _data_frame_of_rolls_and_face_counts: pd.DataFrame -- a data frame of rolls and face counts, where the number of rows and observations is the number of rolls, the number of columns and features is the number of faces, and each cell value is a count of the number of dice for one roll with a face

    Public methods:
        __init__
        generate_data_frame_of_rolls_and_face_counts
        generate_data_frame_of_rolls_and_face_counts_where_all_dice_for_one_roll_have_the_same_face
    '''

    def __init__(self, game):
        '''
        Initializes an Analyzer object with a Game object, and
        infers the data type of each face of each die in the Game object's list of dice
        
        Keyword arguments:
            game: Game -- a Game object

        Return values:
            none

        Side effects:
            Initializes this Analyzer object's Game object

        Exceptions raised:
            none

        Restrictions on when this method can be called:
            May not be called directly
        '''

        self._game = game
        data_frame_of_rolls_and_dice = self._game.show('wide')
        face = data_frame_of_rolls_and_dice.at[0, 0]
        self._type_of_face = type(face)

    #def generate_series_of_face_counts(self, roll):
    #    '''
    #    Generates a series of face counts for a roll
    #
    #    Keyword arguments:
    #        roll: int -- a roll index
    #
    #    Return values:
    #        a series of face counts for a roll
    #
    #    Side effects:
    #        Stores a data frame of rolls and face counts, where the number of rows and observations is the number of rolls, the number of columns and features is the number of faces, and each cell value is a count of the number of dice for one roll with a face
    #
    #    Exceptions raised:
    #        none
    #
    #    Restrictions are when this method can be called:
    #        none
    #    '''
    #
    #    self.generate_data_frame_of_rolls_and_face_counts()
    #    return self._data_frame_of_rolls_and_face_counts.iloc[roll]

    def generate_data_frame_of_rolls_and_face_counts(self):
        '''
        Generates a data frame of rolls and face counts, where the number of rows and observations is the number of rolls, the number of columns and features is the number of faces, and each cell value is a count of the number of dice for one roll with a face

        Keyword arguments:
            none

        Return values:
            a data frame of rolls and face counts, where the number of rows and observations is the number of rolls, the number of columns and features is the number of faces, and each cell value is a count of the number of dice for one roll with a face

        Side effects:
            Stores a data frame of rolls and face counts, where the number of rows and observations is the number of rolls, the number of columns and features is the number of faces, and each cell value is a count of the number of dice for one roll with a face

        Exceptions raised:
            none

        Restrictions are when this method can be called:
            none
        '''

        data_frame_of_rolls_and_dice = self._game.show('wide')
        self._data_frame_of_rolls_and_face_counts = data_frame_of_rolls_and_dice.apply(lambda series_of_faces: series_of_faces.value_counts(), axis = 1).fillna(0).astype(dtype = self._type_of_face).rename_axis(columns = 'face')
        return self._data_frame_of_rolls_and_face_counts

    def generate_data_frame_of_rolls_and_face_counts_where_all_dice_for_one_roll_have_the_same_face(self):
        '''
        Generates a data frame of rolls and face counts where all dice for one roll have the same face

        Keyword arguments:
            none

        Return values:
            a data frame of rolls and face counts where all dice for one roll have the same face

        Side effects:
            Stores a data frame of rolls and face counts where all dice for one roll have the same face

        Exceptions raised:
            none

        Restrictions on when this method can be called:
            none
        '''

        self.generate_data_frame_of_rolls_and_face_counts()
        mask_of_rolls_and_face_counts_greater_than_zero = (self._data_frame_of_rolls_and_face_counts > 0)
        series_of_rolls_and_number_of_faces_with_counts_greater_than_zero = mask_of_rolls_and_face_counts_greater_than_zero.sum(axis = 1)
        self.data_frame_of_rolls_and_face_counts_where_all_dice_for_one_roll_have_the_same_face = self._data_frame_of_rolls_and_face_counts[series_of_rolls_and_number_of_faces_with_counts_greater_than_zero == 1]
        number_of_rolls_with_number_of_faces_with_counts_greater_than_zero_equal_to_one = self.data_frame_of_rolls_and_face_counts_where_all_dice_for_one_roll_have_the_same_face.shape[0]
        return number_of_rolls_with_number_of_faces_with_counts_greater_than_zero_equal_to_one

    def generate_data_frame_of_face_combinations_and_counts(self):
        pass