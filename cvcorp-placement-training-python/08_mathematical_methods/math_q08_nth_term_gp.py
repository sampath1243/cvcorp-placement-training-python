"""
Question 8:
Find the nth term value in the geometric progression series.

Constraints:
n must be > 0 else print "InValid Input."
Output format:
Last term value is : <value>.
"""

a = int(input())
r = int(input())
n = int(input())

if n <= 0:
    print("InValid Input.")
else:
    nt = a * (r ** (n - 1))
    print("Last term value is :", nt, end="")
    print(".")
