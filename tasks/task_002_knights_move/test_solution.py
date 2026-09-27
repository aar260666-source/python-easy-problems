import pytest
from tasks.task_002_knights_move.solution import board_size

@pytest.mark.parametrize("nums,expected", [
    ([3, 2], 1),
    ([31, 34], 293930),
])
def test_board_size(nums, expected):
    assert board_size(nums) == expected

