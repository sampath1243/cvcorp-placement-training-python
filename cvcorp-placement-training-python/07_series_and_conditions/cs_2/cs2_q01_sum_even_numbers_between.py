"""
Q1: Sum of even numbers BETWEEN start and end (exclusive)
If start > end -> "INVALID RANGE"
If no even numbers -> "NO NUMBERS"
"""
s = int(input())
e = int(input())

if s > e:
    print("INVALID RANGE")
else:
    total = 0
    found = False
    for i in range(s + 1, e):
        if i % 2 == 0:
            total += i
            found = True
    if found:
        print(total)
    else:
        print("NO NUMBERS")
