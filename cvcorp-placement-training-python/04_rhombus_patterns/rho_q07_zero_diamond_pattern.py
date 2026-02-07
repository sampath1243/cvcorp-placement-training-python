"""
Rhombus Patterns
Q7: Zero Diamond Pattern

Input: n
Constraint: n > 0 else Invalid Input

Example (n=4):
   0
  0 0
 0 0 0
0 0 0 0
 0 0 0
  0 0
   0
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # top
    for i in range(1, n + 1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(i):
            print("0", end=" ")
        print()

    # bottom
    for i in range(n - 1, 0, -1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(i):
            print("0", end=" ")
        print()
