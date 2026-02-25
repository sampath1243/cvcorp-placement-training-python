"""
Rhombus Patterns
Q5: Alternate Symbol Rhombus (* and #)

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
    *
   # #
  * * *
 # # # #
* * * * *
 # # # #
  * * *
   # #
    *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # top
    for i in range(1, n + 1):
        for s in range(n - i):
            print(" ", end="")
        sym = "*" if i % 2 == 1 else "#"
        for j in range(i):
            print(sym, end=" ")
        print()

    # bottom
    for i in range(n - 1, 0, -1):
        for s in range(n - i):
            print(" ", end="")
        sym = "*" if i % 2 == 1 else "#"
        for j in range(i):
            print(sym, end=" ")
        print()
