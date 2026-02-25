"""
Hollow Patterns - 2
Q4: Butterfly (Double Triangle Mirror)

Input: n
Rule: n > 0 else "Invalid Input"

Example (n=5):
*       *
* *   * *
*   *   *
* *   * *
*       *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == 1 or j == n or j == i or (i + j) == (n + 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()
