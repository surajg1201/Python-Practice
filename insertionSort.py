arr = [12, 11, 13, 5, 6]


def insertion(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1


insertion(arr)
print(arr)
