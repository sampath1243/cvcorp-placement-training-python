"""
Right Angle Patterns - 3
Q3: Same Number Triangle with Starting Value

Input:
rows starting_value

Rules:
- if rows<=0 and starting<0 -> "Invalid Inputs"
- if rows<=0 -> "Invalid Row Value"
- if starting<0 -> "Invalid Starting Value"

Example:
Input: 5 3
Output:
3
44
555
6666
77777
"""

rows, start = map(int, input().split())

if rows <= 0 and start < 0:
    print("Invalid Inputs")
elif rows <= 0:
    print("Invalid Row Value")
elif start < 0:
    print("Invalid Starting Value")
else:
    for i in range(1, rows + 1):
        val = start + (i - 1)
        print(str(val) * i)
