"""
Right Angle Patterns - 3
Q11: Right Shifted Number Triangle

Input: n
Constraint: n > 0 else "Invalid Input"

Example (n=5):
1 2 3 4 5
  2 3 4 5
    3 4 5
      4 5
        5
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for s in range(i - 1):
            print(" ", end=" ")
        for j in range(i, n + 1):
            print(j, end=" ")
        print()
