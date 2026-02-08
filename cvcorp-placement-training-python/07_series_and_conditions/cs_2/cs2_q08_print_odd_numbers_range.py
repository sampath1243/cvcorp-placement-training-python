"""
Q8: Print all odd numbers in range (inclusive)
If start > end -> "INVALID RANGE"
"""
s = int(input())
e = int(input())

if s > e:
    print("INVALID RANGE")
else:
    out = []
    for i in range(s, e + 1):
        if i % 2 != 0:
            out.append(str(i))
    print(" ".join(out))
