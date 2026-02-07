"""
Right Angle Patterns - 2
Q7: Reverse Counting Triangle with Start

Input:
rows
start_value

Constraint:
rows must be > 0 else Invalid Input

Example:
Input:
5
10

Output:
10 9 8 7 6
5 4 3 2
1 0 -1
-2 -3
-4
"""

rows = int(input())
start = int(input())

if rows <= 0:
    print("Invalid Input")
else:
    num = start
    for i in range(rows, 0, -1):
        for j in range(i):
            print(num, end=" ")
            num -= 1
        print()
