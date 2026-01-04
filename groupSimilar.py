test_list = [1, 3, 5, 1, 3, 2, 5, 4, 2]
group_dict = {}

for ele in test_list:
    if ele not in group_dict:
        group_dict[ele] = [ele]
    else:
        group_dict[ele].append(ele)

res = list(group_dict.values())

print(res)
