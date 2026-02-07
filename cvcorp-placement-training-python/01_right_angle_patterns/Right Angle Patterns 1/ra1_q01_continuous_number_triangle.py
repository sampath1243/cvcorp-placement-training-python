"""
Right Angle Patterns - 1
Q1: Continuous Number Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    c = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(c, end=" ")
            c += 1
        print()
