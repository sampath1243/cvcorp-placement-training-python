"""
Rhombus Patterns
Q9: Row Number Repeated Diamond

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
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
            print(i, end=" ")
        print()

    # bottom
    for i in range(n - 1, 0, -1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(i):
            print(i, end=" ")
        print()
