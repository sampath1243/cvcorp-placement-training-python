"""
Right Angle Patterns - 1
Q10: Alphabet Triangle Continuous

Input: n
Rules:
- if n == 0 -> Invalid Input
- if n < 0 -> convert to positive
- range must be 1 to 6 else Range Exceeded

Example (n=4):
A
B C
D E F
G H I J
"""

n = int(input())

if n == 0:
    print("Invalid Input")
else:
    if n < 0:
        n = -n

    if n < 1 or n > 6:
        print("Range Exceeded")
    else:
        ch = 65
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(chr(ch), end=" ")
                ch += 1
            print()
