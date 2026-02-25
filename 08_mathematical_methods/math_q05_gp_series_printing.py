"""
Question 5:
Write a Program to Print first 'n' Numbers in the geometric progression series.

Constraint:
n must be > 0 else print "Invalid Input."
"""

a = int(input())
r = int(input())
n = int(input())

c = 0

if n > 0:
    for i in range(n):
        c += 1
        if c > 1:
            print(", ", end="")
        s = a * (r ** i)
        print(s, end="")
    print(".")
else:
    print("Invalid Input.")
