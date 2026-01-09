""" Second Largest Finder 
Write a program to find the second largest element 
in a list without using built-in max() twice or sorting functions. """
numbers = [10, 5, 20, 8, 15]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)
