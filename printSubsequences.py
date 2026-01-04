def subsequence(arr, ds, idx, n):
    if idx == n:
        print(ds)
        return
    ds.append(arr[idx])
    subsequence(arr, ds, idx+1, n)
    ds.remove(arr[idx])
    subsequence(arr, ds, idx+1, n)


arr = [3, 1, 2]
ds = []
n = len(arr)
subsequence(arr, ds, 0, n)
