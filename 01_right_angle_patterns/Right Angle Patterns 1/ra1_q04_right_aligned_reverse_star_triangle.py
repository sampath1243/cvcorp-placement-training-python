"""
Right Angle Patterns - 1
Q4: Right Aligned Reverse Star Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
****
 ***
  **
   *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n - 1, 0, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(i):
            print("*", end="")
        print()
