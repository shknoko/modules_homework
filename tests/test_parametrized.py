import pytest

from src.bubble_sort import bubble_sort
from src.heap_sort import heap_sort
from src.merge_sort import merge_sort
from src.quick_sort import quick_sort


@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        ([1, 5, 3, 2, 4], [1, 2, 3, 4, 5]),
        ([7, 6, 23423524], [6, 7, 23423524]),
        ([], []),
        ([5], [5]),
        ([5, 4], [4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 2, 1, 3, 3, 3, 3, 3, 3], [1, 2, 3, 3, 3, 3, 3, 3, 3]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([0.11, 0.43, 43.21, -321.54, -11.07], [-321.54, -11.07, 0.11, 0.43, 43.21]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        ([0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]),
        ([12, -100, 47, -123, -5, 1, 0, -3], [-123, -100, -5, -3, 0, 1, 12, 47]),
    ],
)
def test_sort_parametrized(arr, expected):
    heap_sorted = heap_sort(arr)
    quick_sorted = quick_sort(arr)
    merge_sorted = merge_sort(arr)
    bubble_sorted = bubble_sort(arr)

    assert heap_sorted == expected
    assert quick_sorted == expected
    assert merge_sorted == expected
    assert bubble_sorted == expected
