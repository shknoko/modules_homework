def merge_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left: list, right: list) -> list:
    arr = []
    i = o = 0

    while i < len(left) and o < len(right):
        if left[i] <= right[o]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[o])
            o += 1

    arr.extend(left[i:])
    arr.extend(right[o:])

    return arr
