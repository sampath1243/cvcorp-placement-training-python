"""
Question 3:
Write a Program to Print first 'n' Numbers in Harmonic progression series.

Formula:
1/a, 1/(a+d), 1/(a+2d) ... n terms

Constraint:
n must be > 0 else print "Invalid Input"
"""

a = int(input())
d = int(input())
n = int(input())

c = 0

if n > 0:
    for i in range(n):
        c += 1
        if c > 1:
            print(", ", end="")
        s = 1 / (a + i * d)
        print("%.2f" % s, end="")
else:
    print("Invalid Input")
