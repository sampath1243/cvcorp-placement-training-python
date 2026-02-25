"""
Rhombus Patterns
Q4: Multiplication Rhombus Pattern

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
4 8 12 16
3 6 9
2 4
1
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # top
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i * j, end=" ")
        print()

    # bottom
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(i * j, end=" ")
        print()
