"""
Hollow Patterns - 1
Q1: Hollow Square Number Pattern (01 format)

Input: n
Constraint: n > 0 else "Invalid Input"

Example (n=4):
01 02 03 04
05       06
07       08
09 10 11 12
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    c = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # boundary => print number
            if i == 1 or i == n or j == 1 or j == n:
                if c < 10:
                    print("0" + str(c), end=" ")
                else:
                    print(c, end=" ")
            else:
                # inside => spaces (keep width)
                print("  ", end=" ")
            c += 1
        print()
