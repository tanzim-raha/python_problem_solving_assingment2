"""Invert Dictionary"""


d = {"a": 1, "b": 2}
new = {}

for k in d:
    new[d[k]] = k

print(new)
