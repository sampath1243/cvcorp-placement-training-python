"""
Right Angle Patterns - 3
Q1: Floyd Triangle (Right Aligned) with 01 formatting

Input: r
Constraint: r > 0 else "Invalid Input"

Example (r=5):
        01
      02 03
    04 05 06
  07 08 09 10
11 12 13 14 15
"""

r = int(input())

if r <= 0:
    print("Invalid Input")
else:
    c = 0
    for i in range(1, r + 1):
        for j in range(1, r + 1):
            if i + j >= r + 1:
                c += 1
                if c < 10:
                    print("0" + str(c), end=" ")
                else:
                    print(c, end=" ")
            else:
                print("  ", end=" ")
        print()
