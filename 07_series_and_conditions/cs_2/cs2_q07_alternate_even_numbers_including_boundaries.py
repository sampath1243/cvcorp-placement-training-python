"""
Q7: Print all alternative even numbers in range (inclusive)
If no numbers -> "NO NUMBERS"
If start > end -> "INVALID INPUTS"
"""
s = int(input())
e = int(input())

if s > e:
    print("INVALID INPUTS")
else:
    evens = [i for i in range(s, e + 1) if i % 2 == 0]
    alt = evens[0::2]
    if len(alt) == 0:
        print("NO NUMBERS")
    else:
        print(" ".join(str(x) for x in alt))
