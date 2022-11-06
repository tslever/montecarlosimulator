'''
Module for class TestDie, which tests the methods of a Die object
'''

from montecarlosimulator.Die import *
import unittest

class TestDie(unittest.TestCase):
    '''
    Tests the methods of a Die object

    Instance variables:
        none

    Public methods:
        test_init
        test_change_weight
        test_roll
        test_show
    '''

    def _compare_data_frames_of_faces_and_weights(self, array_of_faces):
        '''
        Compares data frames of faces and weights

        Keyword arguments:
            array of faces -- a numpy array of faces. A face must have a data type of string, int, or float. All faces in the numpy array must have the same data type. The faces in the numpy array must be unique.

        Return values:
            none

        Side effects:
            Compares data frames of faces and weights for an numpy arrays of faces

        Exceptions raised:
            AssertionError if a shown data frame of faces and weights does not equal an expected data frame of faces and weights

        Restrictions on when this method can be called:
            none
        '''

        array_of_weights = np.ones(len(array_of_faces))
        expected_data_frame_of_faces_and_weights = pd.DataFrame({'weight': array_of_weights}, index = array_of_faces)
        die = Die(array_of_faces)
        shown_data_frame_of_faces_and_weights = die.show()
        self.assertTrue(shown_data_frame_of_faces_and_weights.equals(expected_data_frame_of_faces_and_weights))

    def test_init(self):
        '''
        Tests Die.__init__

        Keyword arguments:
            none

        Return values:
            none

        Side effects:
            Compares data frames of faces and weights for two numpy arrays of faces

        Exceptions raised:
            AssertionError if a shown data frame of faces and weights does not equal an expected data frame of faces and weights

        Restrictions on when this method can be called:
            none
        '''

        self._compare_data_frames_of_faces_and_weights(np.array([1, 2, 3, 4]))
        self._compare_data_frames_of_faces_and_weights(np.array(['1', '2', '3', '4']))

    def test_change_weight(self):
        '''
        Tests Die.change_weight

        Keyword arguments:
            none

        Return values:
            none

        Side effects:
            Ensures a weight in the data frame of faces and weights of a die is changed,
                    attempting to change the weight corresponding to a face that does not exist in the data frame of faces and weights of a die raises a value error, and
                    attempting to change a weight to a value that cannot be converted to np.float64 raises a value error

        Exceptions raised:
            AssertionError if a weight in the data frame of faces and weights of a die is not changed,
                              attempting to change the weight corresponding to a face that does not exist in the data frame of faces and weights of a die succeeds, or
                              attempting to change a weight to a value that cannot be converted to np.float64 succeeds

        Restrictions on when this method can be called:
            none
        '''

        array_of_faces = [1, 2, 3, 4]
        array_of_weights = np.ones(len(array_of_faces))
        array_of_weights[0] = 2.0
        expected_data_frame_of_faces_and_weights = pd.DataFrame({'weight': array_of_weights}, index = array_of_faces)
        die = Die(array_of_faces)
        die.change_weight(1, 2.0)
        shown_data_frame_of_faces_and_weights = die.show()
        self.assertTrue(shown_data_frame_of_faces_and_weights.equals(expected_data_frame_of_faces_and_weights))

        try:
            die.change_weight('face_that_does_not_exist_in_data_frame_of_faces_and_weights_of_die', 2.0)
            self.fail()
        except ValueError as e:
            pass

        try:
            die.change_weight(1, 'weight_that_cannot_be_converted_to_np.float64')
            self.fail()
        except ValueError as e:
            pass

    def test_roll(self):
        pass

    def test_show(self):
        pass

if __name__ == "__main__":
    verbose = 2
    unittest.main(verbosity = verbose)