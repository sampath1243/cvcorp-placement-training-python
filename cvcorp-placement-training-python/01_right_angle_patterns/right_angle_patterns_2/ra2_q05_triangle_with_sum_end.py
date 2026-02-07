"""
Right Angle Patterns - 2
Q5: Triangle with Sum at End

Input:
rows
start_value

Output:
Print triangle numbers and sum at end of each row.

Example:
Input:
4
1

Output:
1 - 1
2 3 - 5
4 5 6 - 15
7 8 9 10 - 34
"""

rows = int(input())
start = int(input())

if rows <= 0 and start <= 0:
    print("Invalid Inputs")
elif rows <= 0:
    print("Invalid Rows Input")
elif start <= 0:
    print("Invalid Starting Value")
else:
    num = start
    for i in range(1, rows + 1):
        s = 0
        for j in range(i):
            print(num, end=" ")
            s += num
            num += 1
        print("-", s)
