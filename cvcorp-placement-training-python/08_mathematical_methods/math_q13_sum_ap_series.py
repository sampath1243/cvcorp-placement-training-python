"""
Question 13:
Write a Program to Print sum of the first 'n' terms in the Arithmetic progression series.

Constraints:
n must be > 0 else print "Invalid input."

Output format:
term1 + term2 + term3 + ... = sum.
"""

a = int(input())
d = int(input())
n = int(input())

if n <= 0:
    print("Invalid input.")
else:
    t = 0
    for i in range(n):
        term = a + i * d
        t += term

        if i == n - 1:
            print(term, end=" = ")
        else:
            print(term, end=" + ")

    print(t, end=".")
