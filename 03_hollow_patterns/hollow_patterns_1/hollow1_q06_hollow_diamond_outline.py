"""
Hollow Patterns - 1
Q6: Hollow Diamond Outline (simple)

Input: n
Constraint: n > 0 else "Invalid Input"

Example (n=5):
  *
 * *
*   *
 * *
  *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # top half
    for i in range(1, n + 1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # bottom half
    for i in range(n - 1, 0, -1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
