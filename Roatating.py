numbers = [1, 2, 3, 4, 5]
k = 2

for _ in range(k):
    last = numbers.pop()
    numbers.insert(0, last)

print(numbers)
