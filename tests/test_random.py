import pytest
from conftest import random_list  # noqa: F401

from src.bubble_sort import bubble_sort
from src.heap_sort import heap_sort
from src.merge_sort import merge_sort
from src.quick_sort import quick_sort


@pytest.mark.repeat(100)
def test_sort_random(random_list):  # noqa: F811
    expected = sorted(random_list)

    heap_sorted = heap_sort(random_list)
    quick_sorted = quick_sort(random_list)
    merge_sorted = merge_sort(random_list)
    bubble_sorted = bubble_sort(random_list)

    assert heap_sorted == expected
    assert quick_sorted == expected
    assert merge_sorted == expected
    assert bubble_sorted == expected
