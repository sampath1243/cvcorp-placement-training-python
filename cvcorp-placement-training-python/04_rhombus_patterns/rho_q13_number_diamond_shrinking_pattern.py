"""
Rhombus Patterns
Q13: Number Diamond Shrinking Pattern

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
12345
 2345
  345
   45
    5
   45
  345
 2345
12345
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # top half
    for i in range(1, n + 1):
        for s in range(i - 1):
            print(" ", end="")
        for j in range(i, n + 1):
            print(j, end="")
        print()

    # bottom half
    for i in range(n - 1, 0, -1):
        for s in range(i - 1):
            print(" ", end="")
        for j in range(i, n + 1):
            print(j, end="")
        print()
