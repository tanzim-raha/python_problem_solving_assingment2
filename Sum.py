"""Sum of Digits: Write a Python program that takes an integer input from the 
user and calculates the sum of its digits using a while loop."""
num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)
