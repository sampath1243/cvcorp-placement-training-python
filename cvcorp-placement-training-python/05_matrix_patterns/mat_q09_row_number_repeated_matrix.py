"""
Matrix Patterns
Q9: Row Number Repeated Matrix

Input: r c
Constraint: r>0 and c>0 else Invalid Input

Example (3x4):
1 1 1 1
2 2 2 2
3 3 3 3
"""

r = int(input())
c = int(input())

if r <= 0 or c <= 0:
    print("Invalid Input")
else:
    for i in range(1, r + 1):
        for j in range(c):
            print(i, end=" ")
        print()
