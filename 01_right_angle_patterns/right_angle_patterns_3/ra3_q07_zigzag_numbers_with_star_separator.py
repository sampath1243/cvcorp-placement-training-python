"""
Right Angle Patterns - 3
Q7: ZigZag Number Triangle with '*' separator

Input: r
Rules:
- if r==0 -> "Invalid Input"
- if r<0 -> convert to positive

Example (r=5):
1
3*2
4*5*6
10*9*8*7
11*12*13*14*15
"""

r = int(input())

if r == 0:
    print("Invalid Input")
else:
    if r < 0:
        r = -r

    c = 0
    d = 0

    for i in range(1, r + 1):
        if i % 2 == 0:
            d = c + i  # starting point for even rows (descending)

        for j in range(1, i + 1):
            if j != 1:
                print("*", end="")

            c += 1
            if i % 2 == 1:
                print(c, end="")
            else:
                print(d, end="")
                d -= 1

        print()
