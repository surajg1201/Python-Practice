def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [3, 2, 5, 1]
bubbleSort(arr)
print(arr)
