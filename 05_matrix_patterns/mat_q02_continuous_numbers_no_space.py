"""
Matrix Patterns
Q2: Continuous Numbers No Space

Input: n
Constraint: n > 0 else Invalid Input

Example (n=4):
1234
5678
9101112
13141516
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    num = 1
    for i in range(n):
        for j in range(n):
            print(num, end="")
            num += 1
        print()
