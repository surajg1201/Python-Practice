def printSubsequenceSumK(idx, ds, s, targetSum, arr, n):

    if idx == n:
        if targetSum == s:
            print(ds)
        return

    ds.append(arr[idx])
    s += arr[idx]
    printSubsequenceSumK(idx+1, ds, s, targetSum, arr, n)
    s -= arr[idx]
    ds.remove(arr[idx])
    printSubsequenceSumK(idx+1, ds, s, targetSum, arr, n)


arr = [1, 2, 1]
n = len(arr)
ds = []
targetSum = 2
printSubsequenceSumK(0, ds, 0, targetSum, arr, n)
