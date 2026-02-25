"""
Triangle Patterns
Q6: Alphabet Triangle Pyramid

Input: n
Constraint: n > 0 else Invalid Input

Example (n=4):
A
B B
C C C
D D D D
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    ch = 65
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(ch), end=" ")
        ch += 1
        print()
