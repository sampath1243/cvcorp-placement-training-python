"""
Hollow Patterns - 1
Q9: Hollow Right Triangle (edges + base)

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
        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
