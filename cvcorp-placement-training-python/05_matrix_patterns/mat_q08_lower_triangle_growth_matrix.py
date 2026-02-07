"""
Matrix Patterns
Q8: Lower Triangle Growth Matrix

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()
