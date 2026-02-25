"""
Question 4:
Write a Program to Print sum of the first 'n' terms in Harmonic progression series.

Constraint:
n must be > 0 else print "Invalid Input."
"""

a = int(input())
d = int(input())
n = int(input())

sum = 0

if n > 0:
    for i in range(n):
        s = (1 / (a + i * d))
        sum += s
    print("%.2f" % sum)
else:
    print("Invalid Input.")
