s = "This is a python language"

# split the sentence into words
wrds = s.split()

# filter words with even length
even_wrds = [w for w in wrds if len(w) % 2 == 0]

# Join the filtered words back into a sentence
res = " ".join(even_wrds)
print(res)
