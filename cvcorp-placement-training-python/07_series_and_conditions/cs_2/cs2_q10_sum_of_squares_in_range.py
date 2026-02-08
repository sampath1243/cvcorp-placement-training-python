"""
Q10: Sum of squares in range (inclusive)
If start > end -> "INVALID RANGE"
"""
s = int(input())
e = int(input())

if s > e:
    print("INVALID RANGE")
else:
    total = 0
    for i in range(s, e + 1):
        total += i * i
    print(total)
