"""
Right Angle Patterns - 2
Q1: Mixed Increasing/Decreasing Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=6):
1 2 3 4 5 6
5 4 3 2 1
1 2 3 4
3 2 1
1 2
1
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n, 0, -1):
        # odd rows -> increasing
        if i % 2 == 0:
            for j in range(1, i + 1):
                print(j, end=" ")
        else:
            for j in range(i, 0, -1):
                print(j, end=" ")
        print()
