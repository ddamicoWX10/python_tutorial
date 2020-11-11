# Comment in python is #
# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Data types for each column, only non string
types = {'tempout': float, 'windspeed':float, 'windchill':float}

# Initialize data variable
data = {}
for column in columns:
    data[column] = []

# Reading a data file
filename = "data/wxobs20170821.txt"

with open(filename,'r') as datafile:
    # Read first three lines (header)
    for _ in range(3):
        datafile.readline()

    # Read and parse the rest of the file
    for line in datafile:
#        datum = line.split()
#        data.append(datum)
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)

# Compute the function wind chill
def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v16 = v ** 0.16

    wci = a + (b * t) - (c * v16) + (d * t * v16)
    return wci

# Running function to compute wind chill
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

# Debug
for wc_data, wc_comp in zip(data['windchill'],windchill):
    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

# In square brackets, it would essentially be [start:stop:step]
# If nesting, need to have [x][y][z], not[x[y[z]]]
# Python is more sensitive to whitespace (dumb, why?)
# Careful with indentation
# Best practice for reading is with the "with" command
# def = Define function, best practice is to name it a verb statement


