def quickSort(arr, low, high):
    if low <= high:
        pIndex = partition(arr, low, high)
        quickSort(arr, low, pIndex-1)
        quickSort(arr, pIndex+1, high)


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j


arr = [3, 2, 7, 4]
quickSort(arr, 0, len(arr)-1)
print(arr)
