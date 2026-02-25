"""
Matrix Patterns
Q3: Checkerboard 0-1 Pattern

Input: r c
Constraint: r>0 and c>0 else Invalid Input

Example (4x5):
01010
10101
01010
10101
"""

r = int(input())
c = int(input())

if r <= 0 or c <= 0:
    print("Invalid Input")
else:
    for i in range(r):
        for j in range(c):
            if (i + j) % 2 == 0:
                print(0, end="")
            else:
                print(1, end="")
        print()
