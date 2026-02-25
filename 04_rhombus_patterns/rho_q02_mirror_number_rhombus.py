"""
Rhombus Patterns
Q2: Mirror Number Rhombus

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
1 2 3 4 5 4 3 2 1
  2 3 4 5 4 3 2
    3 4 5 4 3
      4 5 4
        5
      4 5 4
    3 4 5 4 3
  2 3 4 5 4 3 2
1 2 3 4 5 4 3 2 1
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # top half
    for i in range(1, n + 1):
        for s in range(i - 1):
            print(" ", end="  ")
        for j in range(i, n + 1):
            print(j, end=" ")
        for j in range(n - 1, i - 1, -1):
            print(j, end=" ")
        print()

    # bottom half
    for i in range(n - 1, 0, -1):
        for s in range(i - 1):
            print(" ", end="  ")
        for j in range(i, n + 1):
            print(j, end=" ")
        for j in range(n - 1, i - 1, -1):
            print(j, end=" ")
        print()
