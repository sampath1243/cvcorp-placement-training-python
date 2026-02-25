"""
Right Angle Patterns - 3
Q6: 0-1 Triangle (no spaces)

Input: n
Rules:
- if n==0 -> "Invalid Input"
- if n<0 -> convert to positive

Example (n=5):
1
01
010
1010
10101
"""

n = int(input())

if n == 0:
    print("Invalid Input")
else:
    if n < 0:
        n = -n

    for i in range(1, n + 1):
        # Start bit pattern matches sample (row-wise)
        start = 1 if (i % 4 == 0 or i % 4 == 1) else 0

        bit = start
        for _ in range(i):
            print(bit, end="")
            bit = 1 - bit
        print()
