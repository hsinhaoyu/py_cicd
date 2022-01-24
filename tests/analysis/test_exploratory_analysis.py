import pytest
import numpy as np
import xyz.analysis.exploratory_analysis as explore

def test_sum_all_default_dataset():
    expected = np.array([[1,2,3,4,5]]).sum()
    assert explore.sum_all_default_dataset() == expected
    
    
