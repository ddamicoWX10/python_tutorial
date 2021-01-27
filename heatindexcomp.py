
from readdata import read_data 

# Comment in python is #
# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex':13}

# Data types for each column, only non string
types = {'tempout': float, 'humout':float, 'heatindex':float}

# Initialize data variable
#data = {}
#for column in columns:
#    data[column] = []

# Reading a data file
#filename = "data/wxobs20170821.txt"
#with open(filename,'r') as datafile:
#    # Read first three lines (header)
#    for _ in range(3):
#        datafile.readline()

#    # Read and parse the rest of the file
#    for line in datafile:
#        datum = line.split()
#        data.append(datum)
#        split_line = line.split()
#        for column in columns:
#            i = columns[column]
#            t = types.get(column, str)
#            value = t(split_line[i])
#            data[column].append(value)

# Read data form file
data = read_data(columns, types=types)

# Compute the function heat index
def compute_heatindex(t, hum):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = 0.22475541
    e = 0.00683783
    f = 0.05481717
    g = 0.00122874
    h = 0.00085282
    i = 0.00000199

    rh = hum / 100.0

    hi = (a + (b * t) + (c * rh) + (d * t * rh) + (e * t**2) + (f * rh**2) +
         (g * t**2 * rh) + (h * t * rh**2) + (i * t**2 * rh**2))

    return hi

# Running function to compute heat index
heatindex = []
for temp, humout in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp, humout))

# Output comparison of data
print('                ORIGINAL  COMPUTED')
print(' DATE    TIME  HEATINDEXL HEATINDEXL DIFFERENCE')
print('------- ------ --------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['heatindex'], heatindex)
for date, time, hi_orig, hi_comp in zip_data:
    hi_diff = hi_orig - hi_comp
    print(f'{date} {time:>6} {hi_orig:9.6f} {hi_comp:9.6f} {hi_diff:10.6f}')

# In square brackets, it would essentially be [start:stop:step]
# If nesting, need to have [x][y][z], not[x[y[z]]]
# Python is more sensitive to whitespace (dumb, why?)
# Careful with indentation
# Best practice for reading is with the "with" command
# def = Define function, best practice is to name it a verb statement


