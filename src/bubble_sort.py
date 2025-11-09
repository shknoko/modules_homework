def bubble_sort(arr: list) -> list:
    arr = arr[:]
    for i in range(len(arr)):
        swapped = False

        for k in range(len(arr) - i - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
                swapped = True

        if not swapped:
            break

    return arr
