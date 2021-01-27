def read_data(columns, types={}, filename="data/wxobs20170821.txt"):
# Keyword arguments can be called in any order
    """
    Read data from CU Boulder weather station data file

    Parameters:
        columns: A dictionary of column names mapping to column indicies
        types: A dictionary of column names mapping to the types which convert each column of data
        filename: A string path pointing to the CU Boulder weather station data file
    """

    # Initialize data variable
    data = {}
    for column in columns:
        data[column] = []

    # Read the data file

    with open(filename,'r') as datafile:
        # Read first three lines (header)
        for _ in range(3):
            datafile.readline()

        # Read and parse the rest of the file
        for line in datafile:
            split_line = line.split()
            for column in columns:
                i = columns[column]
                t = types.get(column, str)
                value = t(split_line[i])
                data[column].append(value)

    return data

