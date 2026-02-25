"""
Hollow Patterns - 2
Q7: Triangle + Butterfly Combination

Input: n
Rule: n > 0 else "Invalid Input"

(First print filled triangle, then butterfly style lines)
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # Part 1: filled pyramid
    for i in range(1, n + 1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(i):
            print("* ", end="")
        print()

    # Part 2: butterfly hollow
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == 1 or j == n or j == i or (i + j) == (n + 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()
