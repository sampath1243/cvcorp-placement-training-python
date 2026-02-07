"""
Right Angle Patterns - 1
Q9: Row Number Repetition Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=7):
1
2 2
3 3 3
4 4 4 4
...
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()
