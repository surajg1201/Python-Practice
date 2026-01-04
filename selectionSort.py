arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]


def selection(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


selection(arr)
print(arr)
