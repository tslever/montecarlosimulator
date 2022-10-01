from Die import Die
import numpy as np
import pandas as pd
import unittest

class TestDie(unittest.TestCase):
    '''
    Tests the methods of a Die object.
    '''

    def compare_data_frames_of_faces_and_weights(self, array_of_faces):
        '''
        Compares data frames of faces and weights.
        Takes an array of faces.
        '''

        array_of_weights = np.ones(len(array_of_faces))
        expected_data_frame_of_faces_and_weights = pd.DataFrame({'weight': array_of_weights}, index = array_of_faces)
        die = Die(array_of_faces)
        shown_data_frame_of_faces_and_weights = die.show()
        self.assertTrue(shown_data_frame_of_faces_and_weights.equals(expected_data_frame_of_faces_and_weights))

    def test_init(self):
        '''
        Tests Die.__init__.
        '''

        self.compare_data_frames_of_faces_and_weights(np.array([1, 2, 3, 4]))
        self.compare_data_frames_of_faces_and_weights(np.array(['1', '2', '3', '4']))

    def test_change_weight(self):
        pass

    def test_roll(self):
        pass

    def test_show(self):
        pass

if __name__ == "__main__":
    unittest.main()