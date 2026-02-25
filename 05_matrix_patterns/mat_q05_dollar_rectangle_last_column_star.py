"""
Matrix Patterns
Q5: Dollar Rectangle with Last Column Star

Input: r c
Constraint: r>0 and c>0 else Invalid Input

Example (4x5):
$ $ $ $ *
$ $ $ $ *
$ $ $ $ *
$ $ $ $ *
"""

r = int(input())
c = int(input())

if r <= 0 or c <= 0:
    print("Invalid Input")
else:
    for i in range(r):
        for j in range(c):
            if j == c - 1:
                print("*", end=" ")
            else:
                print("$", end=" ")
        print()
