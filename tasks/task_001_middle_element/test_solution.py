import pytest
from tasks.task_001_middle_element.solution import get_median

@pytest.mark.parametrize("nums,expected", [
    ([1, 2, 3], 2),
    ([3, 1, 3], 3),
    ([1000, -1000, 0], 0),
    ([10**9 - 1, -10**9 + 1, 0], 0),
])
def test_median(nums, expected):
    assert get_median(nums) == expected