# Description: This script is used to print the version of the libraries that are used in the project.
# import the libraries
import pandas
import numpy
import pytest

# print the version of the libraries just to see if Github actions worked properly
print(f"Pandas version: {pandas.__version__}")
print(f"Numpy version: {numpy.__version__}")
print(f"Pytest version: {pytest.__version__}")