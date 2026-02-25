"""
Hollow Patterns - 2
Q9: Hollow Hourglass Triangle

Input: n
Rule: n > 0 else "Invalid Input"

Example (n=7):
* * * * * * *
  *       *
    *   *
      *
    *   *
  *       *
* * * * * * *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # top inverted
    for i in range(n, 0, -1):
        for s in range(n - i):
            print(" ", end=" ")
        for j in range(1, 2 * i):
            if i == n or i == 1 or j == 1 or j == 2 * i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    # bottom (exclude middle line)
    for i in range(2, n + 1):
        for s in range(n - i):
            print(" ", end=" ")
        for j in range(1, 2 * i):
            if i == n or j == 1 or j == 2 * i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
