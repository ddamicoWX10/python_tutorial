# Comment in python is #
# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2}

# Data types for each column, only non string
types = {'tempout': float}

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

# In square brackets, it would essentially be [start:stop:step]
# If nesting, need to have [x][y][z], not[x[y[z]]]
# Python is more sensitive to whitespace (dumb, why?)
# Careful with indentation
# Best practice for reading is with the "with" command



