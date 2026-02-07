
"""
Right Angle Patterns - 2
Q3: Odd Number Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
1
3 5
7 9 11
13 15 17 19
21 23 25 27 29
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 2
        print()
