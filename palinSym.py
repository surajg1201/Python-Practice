s = "amamat"
pal = True
i, j = 0, len(s)-1
while (i < j):
    if s[i] != s[j]:
        pal = False
        break
    i += 1
    j -= 1

half = len(s)//2
sym = True

for i in range(half):
    if len(s) % 2 == 0:
        if s[i] != s[i+half]:
            sym = False
            break
    else:
        if s[i] != s[i+half+1]:
            sym = False
            break

print("Symmetrical" if sym else "Not Symmetrical")
print("Palindrome" if pal else "Not Palindrome")
