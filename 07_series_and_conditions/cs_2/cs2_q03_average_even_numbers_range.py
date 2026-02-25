"""
Q3: Average of even numbers in range (inclusive)
If start > end -> "INVALID RANGE"
"""
s = int(input())
e = int(input())

if s > e:
    print("INVALID RANGE")
else:
    total = 0
    count = 0
    for i in range(s, e + 1):
        if i % 2 == 0:
            total += i
            count += 1
    # doc doesn’t mention NO NUMBERS here, but safe:
    if count == 0:
        print("NO NUMBERS")
    else:
        print(total / count)
