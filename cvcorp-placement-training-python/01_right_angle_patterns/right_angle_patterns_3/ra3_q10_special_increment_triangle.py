"""
Right Angle Patterns - 3
Q10: Special Increment Triangle (Column-wise filling)

Input: n
Constraint: n > 0 else "Invalid Input"

Example (n=5):
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # Build triangle matrix
    tri = [[0] * (i + 1) for i in range(n)]
    num = 1

    # Fill column-wise (col 0 to col n-1)
    for col in range(n):
        for row in range(col, n):
            tri[row][col] = num
            num += 1

    # Print
    for i in range(n):
        for j in range(i + 1):
            print(tri[i][j], end=" ")
        print()
