# montecarlosimulator
A Python package offering a Monte-Carlo simulator


To install from root of montecarlosimulator: pip install .
To install from GitHub: pip install git+ssh://git@github.com/tslever/montecarlosimulator.git@main#subdirectory=montecarlosimulator


Regarding creating this package: https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/
PEP 8 - Style Guide for Python Code:  https://peps.python.org/pep-0008/#package-and-module-names


Usage Examples

import montecarlosimulator.run_print_hello_world
Hello,World!
from montecarlosimulator import run_print_hello_world
Hello, World!

#import montecarlosimulator.print_hello_world.print_hello_world # does not work after running "python" in CLI
from montecarlosimulator.print_hello_world import print_hello_world
print_hello_world()
Hello, World!

#TODO: Allow using other montecarlosimulator components and tests. Allow using montecarlosimulator as a whole.