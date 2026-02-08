"""
Q6: Print squares with step 2:
s^2, (s+2)^2, ... until value < e
Constraint: inputs > 0 else "Invalid Inputs"
"""
s = int(input())
e = int(input())

if s <= 0 or e <= 0:
    print("Invalid Inputs")
else:
    out = []
    x = s
    while x < e:
        out.append(f"{x}^2")
        x += 2
    print(", ".join(out))
