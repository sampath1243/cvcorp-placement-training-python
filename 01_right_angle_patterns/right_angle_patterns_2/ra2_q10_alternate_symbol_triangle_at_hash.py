"""
Right Angle Patterns - 2
Q10: Alternate Symbol Triangle (@ and #)

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
@
# #
@ @ @
# # # #
@ @ @ @ @
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        for j in range(i):
            if i % 2 == 0:
                print("#", end=" ")
            else:
                print("@", end=" ")
        print()
