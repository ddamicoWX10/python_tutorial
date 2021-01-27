
from readdata import read_data

# Comment in python is #
# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Data types for each column, only non string
types = {'tempout': float, 'windspeed':float, 'windchill':float}

# Read data form file
data = read_data(columns, types=types)

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

# Output comparison of data
print('                ORIGINAL  COMPUTED')
print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
print('------- ------ --------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
for date, time, wc_orig, wc_comp in zip_data:
    wc_diff = wc_orig - wc_comp
    print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')

# In square brackets, it would essentially be [start:stop:step]
# If nesting, need to have [x][y][z], not[x[y[z]]]
# Python is more sensitive to whitespace (dumb, why?)
# Careful with indentation
# Best practice for reading is with the "with" command
# def = Define function, best practice is to name it a verb statement


