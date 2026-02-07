"""
Rhombus Patterns
Q6: Hollow Square with Diagonal

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
*     *
* *   *
*  *  *
*   * *
*     *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n or i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
