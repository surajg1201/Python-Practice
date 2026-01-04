n = int(input())
prev2 = 0
prev = 1
for i in range(2, n+1):
    curi = prev+prev2
    prev2 = prev
    prev = curi
print(prev)
