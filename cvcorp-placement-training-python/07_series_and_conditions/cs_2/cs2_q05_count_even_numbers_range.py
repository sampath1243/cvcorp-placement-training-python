"""
Q5: Count even numbers in range (inclusive)
If start > end -> "INVALID RANGE"
If none -> "NO NUMBERS"
"""
s = int(input())
e = int(input())

if s > e:
    print("INVALID RANGE")
else:
    count = 0
    for i in range(s, e + 1):
        if i % 2 == 0:
            count += 1
    if count == 0:
        print("NO NUMBERS")
    else:
        print(count)
