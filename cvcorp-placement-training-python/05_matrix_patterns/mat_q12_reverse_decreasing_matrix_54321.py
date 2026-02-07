"""
Matrix Patterns
Q12: Reverse Decreasing Matrix 54321

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n):
        for j in range(n, 0, -1):
            print(j, end=" ")
        print()
