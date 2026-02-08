"""
Question 12:
Write a Program to Print sum of the first 'n' terms in the Geometric progression series.

Constraints:
n must be > 0 else print "Invalid Input"
"""

a = int(input())
r = int(input())
n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    if r == 1:
        t = a * n
    else:
        t = a * ((r ** n - 1) // (r - 1))
    print(t)
