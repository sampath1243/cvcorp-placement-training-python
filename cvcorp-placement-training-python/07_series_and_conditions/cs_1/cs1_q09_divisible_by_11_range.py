"""
Q9: Print numbers divisible by 11 in range (inclusive)
If none -> "NO NUMBERS"
If start > end -> "INVALID RANGE"
"""
s = int(input())
e = int(input())

if s > e:
    print("INVALID RANGE")
else:
    found = False
    first = True
    for i in range(s, e + 1):
        if i % 11 == 0:
            if not first:
                print(" ", end="")
            print(i, end="")
            first = False
            found = True
    if not found:
        print("NO NUMBERS")
