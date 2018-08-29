import h5py
import numpy as np
from scipy import stats

# read in the .h5 file
file = h5py.File('BEADS_NK_Dubai_1km_CFLOS_x060.h5', 'r')

# display the keys ('GeoLocation Data', 'CalRawData', etc...)
print(list(file.keys()))

# store one of the keys into a dataset
CalDset = file['CalRawData']
# display the dimensions of that dataset
print(CalDset.shape)
print(CalDset.dtype)

# store the 'CalRawData' into a numpy dataframe
CalNp = file['CalRawData'][...]
print(CalNp.shape)

# find the MAX of the numpy CalNp
maxCal = np.amax(CalNp)
print("max is:", maxCal)

# find the MEAN of the numpy CalNP
meanCal = np.mean(CalNp)
print("mean is:", meanCal)

# display the summary stastistics of the numpy CalNP
print(stats.describe(CalNp))