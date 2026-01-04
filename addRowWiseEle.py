test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)],
             [('for', 5), ('geeks', 1)]]

cus_eles = [6, 7, 8]

res = []

for row_idx, row in enumerate(test_list):
    new_row = []
    for item in row:
        new_item = item + (cus_eles[row_idx],)
        new_row.append(new_item)
    res.append(new_row)
print(res)
