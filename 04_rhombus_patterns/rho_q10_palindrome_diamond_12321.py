"""
Rhombus Patterns
Q10: Palindrome Diamond (12321)

Input: n
Constraint: n > 0 else Invalid Input

Example (n=4):
   1
  121
 12321
1234321
 12321
  121
   1
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # top
    for i in range(1, n + 1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(1, i + 1):
            print(j, end="")
        for k in range(i - 1, 0, -1):
            print(k, end="")
        print()

    # bottom
    for i in range(n - 1, 0, -1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(1, i + 1):
            print(j, end="")
        for k in range(i - 1, 0, -1):
            print(k, end="")
        print()
