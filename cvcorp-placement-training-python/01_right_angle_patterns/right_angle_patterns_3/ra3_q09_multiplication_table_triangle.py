"""
Right Angle Patterns - 3
Q9: Multiplication Triangle

Input: n
Constraint: n must be > 4 else "GiVen Value is Not More Than 4"

Example (n=5):
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
"""

n = int(input())

if n <= 4:
    print("GiVen Value is Not More Than 4")
else:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i * j, end=" ")
        print()
