"""
Hollow Patterns - 1
Q4: Hollow Inverted Triangle Shifted Right

Input: n
Constraint: n > 0 else "Invalid Input"

Example (n=5):
* * * * *
  *     *
    *   *
      * *
        *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n, 0, -1):
        for s in range(n - i):
            print(" ", end=" ")

        for j in range(1, i + 1):
            if i == n or j == 1 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
