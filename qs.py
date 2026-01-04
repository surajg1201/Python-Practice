def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while (i < j):
        while (i <= high-1 and arr[i] <= pivot):
            i += 1
        while (j >= low+1 and arr[j] > pivot):
            j -= 1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def qs(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)
        qs(arr, low, pIndex-1)
        qs(arr, pIndex+1, high)


arr = [5, 3, 2, 7, 0]
qs(arr, 0, len(arr)-1)
print(arr)
