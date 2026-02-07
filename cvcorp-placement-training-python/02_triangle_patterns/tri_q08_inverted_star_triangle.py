"""
Triangle Patterns
Q8: Inverted Star Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
*****
****
***
**
*
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print()
