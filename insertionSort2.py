def iS(arr):
    for i in range(len(arr)):
        j = i
        while (j > 0 and arr[j] < arr[j-1]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1


arr = [6, 3, 7, 4, 2]
iS(arr)
print(arr)
