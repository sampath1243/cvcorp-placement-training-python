"""
Hollow Patterns - 2
Q5: Plus (+) Pattern (Odd & Even middle)

Input: n
Rule: n > 0 else "Invalid Input"

Odd n (5):
    *
    *
* * * * *
    *
    *

Even n (6):
   * *
   * *
* * * * * *
* * * * * *
   * *
   * *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    if n % 2 == 1:
        mid = n // 2 + 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == mid or j == mid:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    else:
        mid1 = n // 2
        mid2 = mid1 + 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == mid1 or i == mid2 or j == mid1 or j == mid2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
