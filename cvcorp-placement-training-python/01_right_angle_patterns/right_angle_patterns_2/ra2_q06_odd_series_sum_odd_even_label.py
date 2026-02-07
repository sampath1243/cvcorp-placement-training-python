"""
Right Angle Patterns - 2
Q6: Odd Series + Sum + Odd/Even Label

Input:
rows
starting_value (must be odd)

Rules:
- if rows <= 0 and starting is not odd -> Invalid Inputs
- if rows <= 0 -> Invalid Row Value
- if starting is even -> Invalid Starting Value

Example:
Input:
4
5

Output:
5 @ 5 - Odd
7 9 @ 16 - Even
11 13 15 @ 39 - Odd
17 19 21 23 @ 80 - Even
"""

rows = int(input())
start = int(input())

if rows <= 0 and start % 2 == 0:
    print("Invalid Inputs")
elif rows <= 0:
    print("Invalid Row Value")
elif start % 2 == 0:
    print("Invalid Starting Value")
else:
    num = start
    for i in range(1, rows + 1):
        s = 0
        for j in range(i):
            print(num, end=" ")
            s += num
            num += 2
        if s % 2 == 0:
            print("@", s, "- Even")
        else:
            print("@", s, "- Odd")
