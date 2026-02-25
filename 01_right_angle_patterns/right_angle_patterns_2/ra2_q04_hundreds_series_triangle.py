"""
Right Angle Patterns - 2
Q4: Hundreds Series Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=4):
100
200 300
400 500 600
700 800 900 1000
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    val = 100
    for i in range(1, n + 1):
        for j in range(i):
            print(val, end=" ")
            val += 100
        print()
