test_list = [
    [('Gfg', 3), ('is', 3)],
    [('best', 1)],
    [('for', 5), ('geeks', 1)]
]

cus_eles = [2, 4, 1]

for i in range(len(test_list)):
    for j in range(len(test_list[i])):
        ele = test_list[i][j]
        word = ele[0]
        num = ele[1]
        new_tuple = (word, num+cus_eles[i])
        test_list[i][j] = new_tuple

print(test_list)
