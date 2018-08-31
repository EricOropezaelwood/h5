'''
Author: Eric Oropezaelwood, Glenn Grant
Date: 31 August 2018
Purpose: Take in an hdf5 file and run statistical calculations across
the columns/frames.
'''
import h5py
import numpy as np
from scipy import stats

# read in the .h5 file
file = h5py.File('BEADS_NK_Dubai_1km_CFLOS_x060.h5', 'r')

# display the keys ('GeoLocation Data', 'CalRawData', etc...)
print(list(file.keys()))
print("")

# store one of the keys into a dataset
CalDset = file['CalRawData']

# display the dimensions of that dataset
print("Shape of dataset:",CalDset.shape)
print("Data type of dataset:", CalDset.dtype)
print("")

# store the 'CalRawData' into a numpy dataframe
CalNp = file['CalRawData'][...]
print("Shape of numpy array:", CalNp.shape)
print("")
print("Numpy array: ")
# np.set_printoptions(suppress=True)
print(CalNp)
print("")

# find the STANDARD DEVIATION of CalNp
stdCalNp = np.std(CalNp, axis = 0) # axis = 0 represents columns
print("Standard Deviation across columns: ")
print(stdCalNp)
print("")

# find the MEAN of the numpy array CalNP
meanCal = np.mean(CalNp, axis = 0) # axis = 0 represents columns
print("Mean across columns is:")
print(meanCal)
print("")

# find the MAX of the numpy array CalNp
maxCal = np.amax(CalNp, axis = 0) # axis = 0 represents columns
print("Max across columns: ")
print(maxCal)
print("")

# find the MIN of the numpy array CalNp
minCal = np.amin(CalNp, axis = 0) # axis = 0 represents columns
print("Min across columns: ")
print(minCal)
print("")

# display the summary stastistics of the numpy array CalNP
#print(stats.describe(CalNp))
