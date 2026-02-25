"""
Hollow Patterns - 1
Q7: Hollow Rectangle

Input: r c
Constraint: r>0 and c>0 else "Invalid Input"

Example (4 6):
* * * * * *
*         *
*         *
* * * * * *
"""

r, c = map(int, input().split())

if r <= 0 or c <= 0:
    print("Invalid Input")
else:
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if i == 1 or i == r or j == 1 or j == c:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
