"""
Right Angle Patterns - 1
Q6: Incremental Number Triangle

Input: n
Constraint: n > 0 else Invalid Input

Example (n=6):
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
