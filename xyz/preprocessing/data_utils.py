"""Some basic utilties for working with data."""
import io
import pkgutil

import pandas as pd


def read_data(filename=None):
    """Read a sample data file.

    If a filename is supplied, read the csv file into a dataframe.
    If not, return a demo dataset.

    I use pkgutil.get_data() to specify the location of the datafile
    inside the package.
    get_data() returns a stream. io.BytesIO() is needed to send it fo pandas.
    """
    if filename is None:
        data_stream = pkgutil.get_data('xyz', 'data/sample_data.csv')
        data = pd.read_csv(io.BytesIO(data_stream), encoding='utf8', sep=',')
    else:
        data = pd.read_csv(filename, sep=',')

    return data
