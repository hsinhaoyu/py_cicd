import numpy as np

import pytest

import xyz.preprocessing.data_utils as data_utils


@pytest.fixture
def temp_data(tmpdir):
    """Create a temp data fixture.
    This uses the tmpdir fixture. It will be deleted automatically
    """
    filename = tmpdir.join('tempdata.csv')
    with open(filename, 'w') as f:
        f.write('A, B, C, D\n'
                '10, 20, 30, 40\n')
    yield filename


class TestReadData(object):

    def test_read_default_dataset(self):
        df = data_utils.read_data()
        assert np.array_equal(df.values, np.array([[1, 2, 3, 4, 5]]))

    def test_on_file(self, temp_data):
        df = data_utils.read_data(temp_data)
        assert np.array_equal(df.values, np.array([[10, 20, 30, 40]]))
