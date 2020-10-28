# Comment in python is #
# Initialize data variable
data = []

# Reading a data file
filename = "data/wxobs20170821.txt"

with open(filename,'r') as datafile:
    # Read first three lines (header)
    for _ in range(3):
        datafile.readline()

    # Read and parse the rest of the file
    for line in datafile:
        datum = line.split()
        data.append(datum)

# In square brackets, it would essentially be [start:stop:step]
# If nesting, need to have [x][y][z], not[x[y[z]]]
# Python is more sensitive to whitespace (dumb, why?)
# Careful with indentation
# Best practice for reading is with the "with" command



