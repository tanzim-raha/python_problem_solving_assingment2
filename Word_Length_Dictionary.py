"""Word Length Dictionary"""
words = ["cat", "apple", "dog"]
d = {}

for w in words:
    d[w] = len(w)

print(d)
