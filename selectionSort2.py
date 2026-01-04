arr = [5, 3, 6, 1, 2, 4]


def SS(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


SS(arr)
print(arr)
