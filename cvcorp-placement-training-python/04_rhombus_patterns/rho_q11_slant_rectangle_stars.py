"""
Rhombus Patterns
Q11: Slant Rectangle Stars

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
*****
 *****
  *****
   *****
    *****
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n):
        for s in range(i):
            print(" ", end="")
        for j in range(n):
            print("*", end="")
        print()
