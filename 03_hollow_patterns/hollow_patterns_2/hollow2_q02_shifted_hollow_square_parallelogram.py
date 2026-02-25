"""
Hollow Patterns - 2
Q2: Shifted Hollow Square (Parallelogram)

Input: n
Rule: n > 0 else "Invalid Input"

Example (n=5):
    * * * * *
   *       *
  *       *
 *       *
* * * * *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        # left shifting spaces
        for s in range(n - i):
            print(" ", end="")
        # hollow square part
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
