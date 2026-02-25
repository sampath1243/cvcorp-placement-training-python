"""
Triangle Patterns
Q9: Palindrome Number Pyramid

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
    1
   2 1 2
  3 2 1 2 3
 4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for s in range(n - i):
            print(" ", end="")

        for j in range(i, 0, -1):
            print(j, end=" ")

        for k in range(2, i + 1):
            print(k, end=" ")

        print()
