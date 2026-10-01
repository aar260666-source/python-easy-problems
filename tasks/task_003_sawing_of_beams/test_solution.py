import pytest
from tasks.task_003_sawing_of_beams.solution import cost_calculation

@pytest.mark.parametrize(
    "l, sections, expected",
    [
        (10, [2, 4, 7], 20),
        (100, [15, 50, 75], 200),
    ]
)

def test_cost_calculation(l, sections, expected):
    result = cost_calculation(l, sections)
    assert result == expected