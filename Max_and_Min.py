t = (3, 7, 1, 9)

mx = t[0]
mn = t[0]

for n in t:
    if n > mx:
        mx = n
    if n < mn:
        mn = n

print(mx, mn)
