"""
Right Angle Patterns - 2
Q8: Mixed Even-Odd Sequence Triangle

Input: n
Rules:
- if n == 0 -> Invalid Input
- if n < 0 -> convert to positive

Example (n=5):
2
3 5
6 8 10
11 13 15 17
18 20 22 24 26
"""

n = int(input())

if n == 0:
    print("Invalid Input")
else:
    if n < 0:
        n = -n

    num = 2
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            if num % 2 == 0:
                num += 1
            else:
                num += 2
        print()
