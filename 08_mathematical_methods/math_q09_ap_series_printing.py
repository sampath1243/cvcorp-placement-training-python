"""
Question 9:
Write a Program to Print first 'n' Numbers in the Arithmetic progression series.

Constraints:
n must be > 0 else print "Invalid Input."
Output ends with "."
"""

a = int(input())
d = int(input())
n = int(input())

if n <= 0:
    print("Invalid Input.")
else:
    for i in range(n):
        t = a + i * d
        if i == n - 1:
            print(t, end=".")
        else:
            print(t, end=", ")
