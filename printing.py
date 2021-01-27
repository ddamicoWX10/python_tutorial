
def print_comparison(name, dates, times, original_data, computed_data):
    """
    Print a comparison of two time series (original and computed)

    Parameters:
        name: String name for data being compared (limited to 9 char)
        dates: List of strings representing dates for each data
        times: List of strings representing times for each data
        original_data: List of original data (floating point)
        computed_data: List of computed data (floats)
    """
    # Output comparison of data
    print('                ORIGINAL  COMPUTED')
    print(f' DATE    TIME  {name.upper():>9} {name.upper():>9} DIFFERENCE')
    print('------- ------ --------- --------- ----------')
    zip_data = zip(dates, times, original_data, computed_data)
    for date, time, orig, comp in zip_data:
        print(f'{date} {time:>6} {orig:9.6f} {comp:9.6f} {orig-comp:10.6f}')
