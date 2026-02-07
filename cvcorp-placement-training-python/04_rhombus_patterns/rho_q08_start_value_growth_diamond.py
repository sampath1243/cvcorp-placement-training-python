"""
Rhombus Patterns
Q8: Start Value Growth Diamond

Input:
rows
start

Example (rows=5 start=3):
3
44
555
6666
77777
6666
555
44
3
"""

rows = int(input())
start = int(input())

if rows <= 0:
    print("Invalid Input")
else:
    # top
    for i in range(1, rows + 1):
        val = start + (i - 1)
        print(str(val) * i)

    # bottom
    for i in range(rows - 1, 0, -1):
        val = start + (i - 1)
        print(str(val) * i)
