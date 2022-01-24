from ..preprocessing import data_utils

def sum_all(df):
    vals = df.values
    return vals.sum()

def sum_all_default_dataset():
    df = data_utils.read_data()
    return sum_all(df)
