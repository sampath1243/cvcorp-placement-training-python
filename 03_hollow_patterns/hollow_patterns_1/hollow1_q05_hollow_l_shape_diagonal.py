"""
Hollow Patterns - 1
Q5: Hollow L Shape + Diagonal

Input: n
Constraint: n > 0 else "Invalid Input"

Typical shape:
*
*     *
*   *
*
*
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # left border OR diagonal (i+j==n+1) OR first row
            if j == 1 or (i + j == n + 1) or i == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
