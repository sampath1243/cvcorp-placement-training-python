"""
Right Angle Patterns - 1
Q8: Even Numbers Reverse Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
10 10 10 10 10
8 8 8 8
6 6 6
4 4
2
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    val = n * 2
    for i in range(n, 0, -1):
        for j in range(i):
            print(val, end=" ")
        print()
        val -= 2
