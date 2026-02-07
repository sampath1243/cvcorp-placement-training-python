"""
Right Angle Patterns - 1
Q3: Reverse @ Triangle

Input: n
Rules:
- if n == 0 -> Invalid Input
- if n < 0 -> convert to positive

Example (n=5):
@ @ @ @ @
@ @ @ @
@ @ @
@ @
@
"""

n = int(input())

if n == 0:
    print("Invalid Input")
else:
    if n < 0:
        n = -n

    for i in range(n, 0, -1):
        for j in range(i):
            print("@", end=" ")
        print()
