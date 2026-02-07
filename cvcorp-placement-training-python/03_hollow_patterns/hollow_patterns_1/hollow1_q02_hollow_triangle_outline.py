"""
Hollow Patterns - 1
Q2: Hollow Triangle Outline

Input: n
Constraint: n > 0 else "Invalid Input"

Example (n=5):
    *
   * *
  *   *
 *     *
* * * * *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for s in range(n - i):
            print(" ", end="")

        for j in range(1, 2 * i):
            if i == n or j == 1 or j == (2 * i - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()
