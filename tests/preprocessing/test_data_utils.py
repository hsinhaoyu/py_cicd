import numpy as np
import pytest
import xyz.preprocessing.data_utils as data_utils

def test_read_data():
    data = data_utils.read_data()
    print(data.values)
    assert np.array_equal(data.values, np.array([[1,2,3,4,5]]))
