"""
Rhombus Patterns
Q3: Start Value Rhombus Numbers

Input:
rows
start

Example:
rows=4 start=2
2
3 3
4 4 4
5 5 5 5
5 5 5 5
4 4 4
3 3
2
"""

rows = int(input())
start = int(input())

if rows <= 0:
    print("Invalid Input")
else:
    # top
    for i in range(rows):
        val = start + i
        for j in range(i + 1):
            print(val, end=" ")
        print()

    # bottom
    for i in range(rows - 1, -1, -1):
        val = start + i
        for j in range(i + 1):
            print(val, end=" ")
        print()
