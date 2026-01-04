s = "Geeks for geeks"

words = s.split()

reversed_words = ""
for word in reversed(words):
    reversed_words += word + " "

print(reversed_words)
