def sub_mat_even(n):
    num = 1
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(num)
            num += 1

        if i % 2 == 1:
            row.reverse()

        matrix.append(row)

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()


sub_mat_even(2)
