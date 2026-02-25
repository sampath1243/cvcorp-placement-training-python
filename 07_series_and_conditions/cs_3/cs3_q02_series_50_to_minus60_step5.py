"""
Q2: Print 5*s, 5*(s+1), ... 5*e (step 5)
Format:
- positives normal
- negatives in parentheses like (-5)
Separated by ", "
"""
s = int(input())
e = int(input())

out = []
step = 1 if s < e else -1

i = s
while True:
    val = 5 * i
    if val < 0:
        out.append(f"({val})")
    else:
        out.append(str(val))
    if i == e:
        break
    i += step

print(", ".join(out))
