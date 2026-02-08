"""
Q7: Print all even numbers in range (inclusive)
If start > end -> "INVALID RANGE"
Output example: 2 4 6 8 10
"""
s = int(input())
e = int(input())

if s > e:
    print("INVALID RANGE")
else:
    first = True
    for i in range(s, e + 1):
        if i % 2 == 0:
            if not first:
                print(" ", end="")
            print(i, end="")
            first = False
