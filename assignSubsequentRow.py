test_list = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

print("The original list:" + str(test_list))

a = test_list[0]
b = test_list[1:len(test_list)]
d = dict()
for i in range(0, len(a)):
    d[a[i]] = b[i]

print("Assigned Matrix: " + str(d))
