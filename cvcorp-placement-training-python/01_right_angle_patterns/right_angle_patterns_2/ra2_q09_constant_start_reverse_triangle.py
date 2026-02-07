"""
Right Angle Patterns - 2
Q9: Constant Start Reverse Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n, 0, -1):
        for j in range(n, n - i, -1):
            print(j, end=" ")
        print()
