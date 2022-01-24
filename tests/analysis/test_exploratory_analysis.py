import numpy as np

import pandas as pd

import pytest

import xyz.analysis.exploratory_analysis as explore

tmpdata = {'a': 1, 'b': 2, 'c': 3}


def read_data_bug_free():
    return pd.DataFrame([tmpdata])


def test_sum_all():
    df = read_data_bug_free()
    expected = sum(tmpdata.values())
    assert explore.sum_all(df) == expected


def test_sum_all_default_dataset(mocker):
    """Note that the mocker fixture is from pytest-mock."""
    expected = sum(tmpdata.values())

    read_data_mock = mocker.patch(
        'xyz.preprocessing.data_utils.read_data',
        side_effect=read_data_bug_free
    )

    assert explore.sum_all_default_dataset() == expected
