

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while (i < j):
        while (i <= high and arr[i] <= pivot):
            i += 1
        while (j >= low and arr[j] > pivot):
            j -= 1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]

    return j


def qs(arr, low, high):

    if (low < high):
        partIdx = partition(arr, low, high)
        qs(arr, low, partIdx-1)
        qs(arr, partIdx+1, high)


arr = [1, 7, 4, 1, 10, 9, -2]
qs(arr, 0, len(arr)-1)
print(arr)
