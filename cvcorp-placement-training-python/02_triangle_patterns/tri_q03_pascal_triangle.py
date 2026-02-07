"""
Triangle Patterns
Q3: Pascal Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n):
        for s in range(n - i - 1):
            print(" ", end="")

        val = 1
        for j in range(i + 1):
            print(val, end=" ")
            val = val * (i - j) // (j + 1)

        print()
