
from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_heatindex

# Comment in python is #
# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex':13}

# Data types for each column, only non string
types = {'tempout': float, 'humout':float, 'heatindex':float}

# Read data form file
data = read_data(columns, types=types)

# Running function to compute heat index
heatindex = [compute_heatindex(t,h) for t, h in zip(data['tempout'],data['humout'])]

#heatindex = []
#for temp, humout in zip(data['tempout'], data['humout']):
#    heatindex.append(compute_heatindex(temp, humout))

# Output comparison of data
print_comparison('HEAT INDX', data['date'], data['time'], data['heatindex'], heatindex)

