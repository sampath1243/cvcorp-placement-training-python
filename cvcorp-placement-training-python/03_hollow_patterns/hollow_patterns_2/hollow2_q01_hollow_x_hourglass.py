"""
Hollow Patterns - 2
Q1: Hollow X (Hourglass X)

Input: n
Rules:
- n > 0 else "Invalid Input"

Example (n=7):
*     *
 *   *
  * *
   *
  * *
 *   *
*     *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or (i + j) == (n + 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()
