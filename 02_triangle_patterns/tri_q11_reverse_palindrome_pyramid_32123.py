"""
Triangle Patterns
Q11: Reverse Palindrome Pyramid (32123)

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
123454321
 1234321
  12321
   121
    1
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n, 0, -1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(1, i + 1):
            print(j, end="")
        for k in range(i - 1, 0, -1):
            print(k, end="")
        print()
