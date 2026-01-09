"""Frequency Counter"""
nums = [1, 2, 2, 3, 1]
freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)
