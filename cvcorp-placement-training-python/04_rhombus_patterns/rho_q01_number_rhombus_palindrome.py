"""
Rhombus Patterns
Q1: Number Rhombus Palindrome

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
5
454
34543
2345432
123454321
2345432
34543
454
5
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # top part
    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            print(j, end="")
        for k in range(n - 1, i - 1, -1):
            print(k, end="")
        print()

    # bottom part
    for i in range(2, n + 1):
        for j in range(i, n + 1):
            print(j, end="")
        for k in range(n - 1, i - 1, -1):
            print(k, end="")
        print()
