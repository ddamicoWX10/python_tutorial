# Comment in python is #
# Reading a data file

filename = "data/wxobs20170821.txt"

with open(filename,'r') as datafile:
    data = datafile.read()
# Python is more sensitive to whitespace (dumb, why?)
# Careful with indentation
# Best practice for reading is with the "with" command


