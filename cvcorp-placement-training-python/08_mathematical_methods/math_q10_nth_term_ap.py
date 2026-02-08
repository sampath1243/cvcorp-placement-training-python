"""
Question 10:
Find and Print the nth term value in the Arithmetic progression series.

Constraints:
n must be > 0 else print "InValid Input."
Output format:
Last term value is : <value>.
"""

a = int(input())
d = int(input())
n = int(input())

if n <= 0:
    print("InValid Input.")
else:
    nt = a + (n - 1) * d
    print("Last term value is :", nt, end=".")
