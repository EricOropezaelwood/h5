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
	# print("Numpy array: ")
	# np.set_printoptions(suppress=True) # suppress scientific data
	print(outputNp)
	print("")
	return outputNp

# Take in an array and run STD, MEAN, MAX and MIN across columns
def statisticsAcrossColumns(inputArray):

	# find the STANDARD DEVIATION of CalNp (ignoring NaN values)
	stdArray = np.nanstd(inputArray, axis = 0) # axis = 0 represents columns
	print("Standard Deviation across columns: ")
	print(stdArray)
	print("")

	# find the MEAN of the numpy array CalNP (ignoring NaN values)
	meanArray = np.nanmean(inputArray, axis = 0) # axis = 0 represents columns
	print("Mean across columns is:")
	print(meanArray)
	print("")

	# find the MAX of the numpy array CalNp (ignoring NaN values)
	maxArray = np.nanmax(inputArray, axis = 0) # axis = 0 represents columns
	print("Max across columns: ")
	print(maxArray)
	print("")

	# find the MIN of the numpy array CalNp (ignoring NaN values)
	minArray = np.nanmin(inputArray, axis = 0) # axis = 0 represents columns
	print("Min across columns: ")
	print(minArray)
	print("")


# read in the .h5 file
h5File = h5py.File('CFLOS.h5', 'r+') #ONLY RUN ONCE PER FILE!!!

# display the keys ('GeoLocation Data', 'CalRawData', etc...)
print(list(h5File.keys()))
print("")

'''
# store one of the keys into a dataset
FirstDset = h5File['CalRawData']

# display the dimensions of that dataset
print("Shape of dataset:",FirstDset.shape)
print("Data type of dataset:", FirstDset.dtype)
print("")
'''

# convert one dataset to numpy array 
CalNp = datasetToNumpyArray(h5File)
print(CalNp)
print("")

'''
# find the STANDARD DEVIATION of CalNp (ignoring NaN values)
for i in range(10800):
	stdArray2 = np.nanstd(CalNp[i], axis = 0)

print(stdArray2)
'''


meanArray = np.nanmean(CalNp, axis = 0) # axis = 0 represents columns
print("Mean across columns: ")
print(meanArray)
print("")




# SECOND TRY
del h5File['CalRawData']

# NEED TO ALTER THE SHAPE OF THE ARRAY stdArray (implement own standard deviation function across 10800 stacks of images)
dset = h5File.create_dataset('CalRawData', data=meanArray)


# call the stastics function
# statisticsAcrossColumns(CalNp)
