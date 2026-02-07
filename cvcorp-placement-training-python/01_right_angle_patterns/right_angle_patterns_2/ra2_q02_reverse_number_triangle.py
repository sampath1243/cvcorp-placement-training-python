"""
Right Angle Patterns - 2
Q2: Reverse Decreasing Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
