import random


def quick_sort(arr: list) -> list:
    if not isinstance(arr, list):
        raise TypeError("Передан не список")

    if len(arr) < 2:
        return arr

    arr = arr[:]

    def _quick_sort(arr: list, left: int, right: int) -> None:

        if left >= right:
            return None

        random_index = random.randint(left, right)
        arr[random_index], arr[left] = arr[left], arr[random_index]

        i = left
        new_left, new_right = left, right
        pivot = arr[left]

        while i <= new_right:
            if arr[i] < pivot:
                arr[new_left], arr[i] = arr[i], arr[new_left]
                new_left += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[new_right] = arr[new_right], arr[i]
                new_right -= 1
            else:
                i += 1

        _quick_sort(arr, left, new_left - 1)
        _quick_sort(arr, new_right + 1, right)

    _quick_sort(arr, 0, len(arr) - 1)

    return arr
