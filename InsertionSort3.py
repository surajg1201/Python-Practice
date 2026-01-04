def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1


arr = [5, 9, 2, 1, 3]
insertionSort(arr)
print(arr)
