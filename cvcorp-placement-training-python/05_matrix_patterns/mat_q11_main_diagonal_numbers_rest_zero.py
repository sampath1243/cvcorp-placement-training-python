"""
Matrix Patterns
Q11: Main Diagonal Numbers, Rest 0

Input: n
Constraint: n > 0 else Invalid Input

Example (n=4):
1 0 0 0
0 2 0 0
0 0 3 0
0 0 0 4
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                print(i, end=" ")
            else:
                print(0, end=" ")
        print()
