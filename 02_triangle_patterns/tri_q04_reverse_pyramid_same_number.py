"""
Triangle Patterns
Q4: Reverse Pyramid Same Number

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
1 1 1 1 1
 2 2 2 2
  3 3 3
   4 4
    5
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for s in range(i - 1):
            print(" ", end="")
        for j in range(n - i + 1):
            print(i, end=" ")
        print()
