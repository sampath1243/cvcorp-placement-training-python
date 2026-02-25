"""
Q1: Print all multiples of 100 from start to end (inclusive)
Constraint: both inputs > 0 else "Invalid Inputs"
"""
s = int(input())
e = int(input())

if s <= 0 or e <= 0:
    print("Invalid Inputs")
else:
    if s > e:
        s, e = e, s
    out = []
    for i in range(s, e + 1):
        if i % 100 == 0:
            out.append(str(i))
    print(", ".join(out))
