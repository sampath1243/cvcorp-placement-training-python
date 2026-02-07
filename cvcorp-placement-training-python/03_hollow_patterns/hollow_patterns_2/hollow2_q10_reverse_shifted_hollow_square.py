"""
Hollow Patterns - 2
Q10: Reverse Shifted Hollow Square

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
        for s in range(i - 1):
            print(" ", end="")
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
