"""
Triangle Patterns
Q2: Floyd Triangle with 01 formatting

Input: n
Constraint: n > 0 else Invalid Input

Example (n=4):
01
02 03
04 05 06
07 08 09 10
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    c = 1
    for i in range(1, n + 1):
        for j in range(i):
            if c < 10:
                print("0" + str(c), end=" ")
            else:
                print(c, end=" ")
            c += 1
        print()
