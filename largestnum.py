#1. Largest among Three Numbers: Write a Python program that takes 
# three numbers as input and prints out the largest among them.

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")
    