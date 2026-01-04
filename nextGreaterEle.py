# find the next greater ele of all the elements in the array

def nextGreaterEle(arr):
    st = []
    nge = [-1]*len(arr)

    for i in range(len(arr)-1, -1, -1):
        while st and st[-1] <= arr[i]:
            st.pop()
        if st:
            nge[i] = st[-1]

        st.append(arr[i])
    return nge


arr = [1, 3, 4, 2]
ls = nextGreaterEle(arr)
print(ls)
