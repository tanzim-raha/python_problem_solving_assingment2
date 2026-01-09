"""Number Reverser: Write a Python program that takes an integer input from the user
and prints its reverse using a while loop"""
n = int(input("Enter a number: "))
r = 0

while n > 0:
    d= n % 10
    r= r * 10 + d
    n //= 10

print("Reversed number:", r)
