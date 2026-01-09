"""Positive and Negative Split
Given a list of integers, separate them into two lists: one with positive numbers and
another with negative numbers."""
number=[1,2,-3,4,-5,-2,5,7,-9,-7,8,-8,-1,0]

positive_num=[]
negative_num=[]

for num in number:
    if num>0:
        positive_num.append(num)
    elif num <0:
        negative_num.append(num)
        
print("P = ",positive_num)
print("N = ",negative_num)
