"""Module for exploratory data analysis."""
from ..preprocessing import data_utils


def sum_all(df):
    """Sum all values in the dataframe df.

    args:
        df: a Pandas dataframe

    returns:
        A numerical value
    """
    vals = df.values
    return vals.sum()


def sum_all_default_dataset():
    """Read the default dataset, and then calculate sum."""
    df = data_utils.read_data()
    return sum_all(df)
