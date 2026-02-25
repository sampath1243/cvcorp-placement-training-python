"""
Q3: Print series in format:
5*s, 5*(s-1), ... as "5*10, 5*9, ... 5*(-1) ..."
Negatives must be like 5*(-2)
Separated by ", "
"""
s = int(input())
e = int(input())

out = []
step = 1 if s < e else -1

i = s
while True:
    if i < 0:
        out.append(f"5*({i})")
    else:
        out.append(f"5*{i}")

    if i == e:
        break
    i += step

print(", ".join(out))
