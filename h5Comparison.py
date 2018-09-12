import h5py
import numpy as np
from scipy import stats

# read in the .h5 file
h5File = h5py.File('CFLOS.h5', 'r')

# display the keys ('GeoLocation Data', 'CalRawData', etc...)
print(list(h5File.keys()))
print("")

# store one of the keys into a dataset
FirstDset = h5File['CalRawData']

# display the dimensions of that dataset
print("Shape of dataset:",FirstDset.shape)
print("Data type of dataset:", FirstDset.dtype)
print("")
print(FirstDset)
print("")

# store the 'CalRawData' into a numpy dataframe
outputNp1 = h5File['CalRawData'][...]
print(outputNp1)
print("")


# read in the .h5 file
h5File2 = h5py.File('DONOTALTER.h5', 'r')
print(list(h5File2.keys()))
print("")

# store one of the keys into a dataset
SecondDset = h5File['CalRawData']

# display the dimensions of that dataset
print("Shape of dataset:",SecondDset.shape)
print("Data type of dataset:", SecondDset.dtype)
print("")
print(SecondDset)

# store the 'CalRawData' into a numpy dataframe
outputNp2 = h5File2['CalRawData'][...]
print(outputNp2)
print("")

print(np.array_equiv(outputNp1,outputNp2))
'''
array1 = [1,2,3,4]
array2 = [2,3,4,5]

print(np.array_equal(array1,array2))
'''