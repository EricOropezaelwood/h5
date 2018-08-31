'''
Author: Eric Oropezaelwood, Glenn Grant
Date: 31 August 2018
Purpose: Take in an hdf5 file and run statistical calculations across
the columns/frames.
'''
import h5py
import numpy as np
from scipy import stats

# Take in a file and convert one of the datasets to an array
def datasetToNumpyArray(inputFile):

	# store the 'CalRawData' into a numpy dataframe
	outputNp = inputFile['CalRawData'][...]
	print("Shape of numpy array from dataset 'CalRawData':", outputNp.shape)
	print("")
	print("Numpy array: ")
	# np.set_printoptions(suppress=True) # suppress scientific data
	print(outputNp)
	print("")
	return outputNp

# Take in an array and run STD, MEAN, MAX and MIN across columns
def statisticsAcrossColumns(inputArray):

	# find the STANDARD DEVIATION of CalNp
	stdArray = np.std(inputArray, axis = 0) # axis = 0 represents columns
	print("Standard Deviation across columns: ")
	print(stdArray)
	print("")

	# find the MEAN of the numpy array CalNP
	meanArray = np.mean(inputArray, axis = 0) # axis = 0 represents columns
	print("Mean across columns is:")
	print(meanArray)
	print("")

	# find the MAX of the numpy array CalNp
	maxArray = np.amax(inputArray, axis = 0) # axis = 0 represents columns
	print("Max across columns: ")
	print(maxArray)
	print("")

	# find the MIN of the numpy array CalNp
	minArray = np.amin(inputArray, axis = 0) # axis = 0 represents columns
	print("Min across columns: ")
	print(minArray)
	print("")


# read in the .h5 file
h5File = h5py.File('BEADS_NK_Dubai_1km_CFLOS_x060.h5', 'r')

# display the keys ('GeoLocation Data', 'CalRawData', etc...)
print(list(h5File.keys()))
print("")
'''
# store one of the keys into a dataset
CalDset = h5File['CalRawData']

# display the dimensions of that dataset
print("Shape of dataset:",CalDset.shape)
print("Data type of dataset:", CalDset.dtype)
print("")
'''

# convert one dataset to numpy array 
CalNp = datasetToNumpyArray(h5File)

# call the stastics function
statisticsAcrossColumns(CalNp)

# display the summary stastistics of the numpy array CalNP
#print(stats.describe(CalNp))
