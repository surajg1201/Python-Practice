A = [[1, 2], [3, 4]]
B = [[4, 5], [6, 7]]

print("printing elements of first matrix: ")

for row in A:
    for ele in row:
        print(ele, end=" ")
    print()

print("printing elements of second matrix: ")

for row in B:
    for ele in row:
        print(ele, end=" ")
    print()

# add

result = [[0, 0], [0, 0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print("Addition of two matrix: ")
for row in result:
    for ele in row:
        print(ele, end=" ")
    print()

# sub
result = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] - B[i][j]

print("Subtraction of two matrix: ")
for row in result:
    for ele in row:
        print(ele, end=" ")
    print()
