
from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_windchill

# Comment in python is #
# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Data types for each column, only non string
types = {'tempout': float, 'windspeed':float, 'windchill':float}

# Read data form file
data = read_data(columns, types=types)

# Running function to compute wind chill
windchill = [compute_windchill(t,w) for t, w in zip(data['tempout'], data['windspeed'])]

#windchill = []
#for temp, windspeed in zip(data['tempout'], data['windspeed']):
#    windchill.append(compute_windchill(temp, windspeed))

print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)

