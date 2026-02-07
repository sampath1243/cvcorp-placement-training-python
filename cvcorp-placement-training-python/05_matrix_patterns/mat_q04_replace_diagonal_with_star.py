"""
Matrix Patterns
Q4: Replace Main Diagonal with *

Input: n
Constraint: n > 0 else Invalid Input

Example (n=4):
* 2 3 4
5 * 7 8
9 10 * 12
13 14 15 *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    num = 1
    for i in range(n):
        for j in range(n):
            if i == j:
                print("*", end=" ")
            else:
                print(num, end=" ")
            num += 1
        print()
