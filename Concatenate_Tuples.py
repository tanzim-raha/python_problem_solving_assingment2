t1 = (1, 2)
t2 = (3, 4)

t = ()
for x in t1:
    t += (x,)
for x in t2:
    t += (x,)

print(t)
