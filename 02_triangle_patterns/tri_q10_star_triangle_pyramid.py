"""
Triangle Patterns
Q10: Star Pyramid

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
    *
   * *
  * * *
 * * * *
* * * * *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for s in range(n - i):
            print(" ", end="")

        for j in range(i):
            print("*", end=" ")

        print()
