"""
Q6: Print Alternative Even Numbers between given numbers (inclusive)
Constraint: both inputs > 0 else "Invalid Inputs"
"""
s = int(input())
e = int(input())

if s <= 0 or e <= 0:
    print("Invalid Inputs")
else:
    if s > e:
        s, e = e, s

    evens = [i for i in range(s, e + 1) if i % 2 == 0]
    alt = evens[0::2]
    if len(alt) == 0:
        print("NO NUMBERS")
    else:
        print(" ".join(str(x) for x in alt))
