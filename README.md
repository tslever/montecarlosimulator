# montecarlosimulator
A Python package offering a Monte-Carlo simulator
Created: 10/01/22 by Tom Lever
Updated: 12/01/22 by Tom Lever

## Metadata
Author: Tom Lever
Project name: Monte Carlo Simulator

## Synopsis

### Creating montecarlosimulator

Regarding creating this package: https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/
PEP 8 - Style Guide for Python Code:  https://peps.python.org/pep-0008/#package-and-module-names
PEP 257 - Docstring Conventions: https://peps.python.org/pep-0257/

### Installing

To install from root of `montecarlosimulator`: `pip install .`
To install from GitHub: `pip install git+ssh://git@github.com/tslever/montecarlosimulator.git@main`

## Importing

To import class `Die`, run `from montecarlosimulator import Die` or `from montecarlosimulator.montecarlo import Die`.

## Creating dice

Run the following code to
* create a die,
* show the die's data frame of faces and weights,
* change a weight of a face of the die,
* show the die's data frame of faces and weights,
* roll the die and acquire a list of rolled faces, and
* display the list of rolled faces.

>>> import numpy as np
>>> from montecarlosimulator import Die
>>> array_of_faces = np.array(['A', 'B', 'C'], dtype = str)
>>> die = Die(array_of_faces)
>>> die.show()
  face  weight
0    A     1.0
1    B     1.0
2    C     1.0
>>> die.change_weight(face = 'A', weight = 2.0)
>>> die.show()
  face  weight
0    A     2.0
1    B     1.0
2    C     1.0
>>> list_of_rolled_faces = die.roll(number_of_rolls = 3)
>>> list_of_rolled_faces
['B', 'C', 'A']

## Playing games

## API description

### Die

#### Description

A die may be rolled to select a face.
A die has $N$ sides.
Each side is associated with a face and a weight.
Weights default to 1.0 and may be changed.
A face has a data type of str, int, or float.
All faces have the same data type.
The faces must be unique.
A weight has a data type of float.

#### Public methods

__init__
change_weight
roll
show

##### __init__

###### Docstring

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

###### Keyword arguments

array_of_faces: np.ndarray -- a 1D numpy array of faces. A face must have a data type of str, int, or float. All faces in the numpy array have the same data type. The faces in the numpy array must be unique.

###### Return values

none

##### change_weight

###### Docstring

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

###### Keyword arguments

face: str, int, np.float64 -- A string, integer, or floating-point number
weight: np.float64 -- A numpy floating-point number

###### Return values

none

##### roll

###### Docstring

Rolls this Die object one or more times

Keyword arguments:
    number_of_rolls: int -- An integer. Defaults to 1.

Return values:
    list_of_rolled_faces: list -- A list of rolled faces

Side effects:
    Samples rows from the data frame of faces and weights of this Die object according to the weights

Exceptions raised:
    none

Restrictions on when this method can be called:
    none

###### Keyword arguments

number_of_rolls: int -- An integer. Defaults to 1.

###### Return values

list_of_rolled_faces: list -- A list of rolled faces

##### show

###### Docstring

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

###### Keyword arguments

none

###### Return values

_data_frame_of_faces_and_weights: pd.DataFrame -- The data frame of faces and weights of this Die object