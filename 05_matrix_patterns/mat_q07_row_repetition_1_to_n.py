"""
Matrix Patterns
Q7: Row Repetition 1 to N

Input: n
Constraint: n > 0 else Invalid Input

Example (n=4):
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(n):
            print(i, end=" ")
        print()
