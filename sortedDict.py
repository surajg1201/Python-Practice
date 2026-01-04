d = {'c': 2, 'a': 1, 'd': 3}
my_Keys = list(d.keys())
my_Keys.sort()
sd = {}
for i in my_Keys:
    sd[i] = d[i]
print(sd)
