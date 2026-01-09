t = (1, 2, 3, 4)

for i in range(len(t)):
    for j in range(i+1, len(t)):
        if (t[i] + t[j]) % 2 == 0:
            print(t[i], t[j])
