"""
Q5: Print pairs like:
10@9, 9@8, 8@7, ... , -5@-6  (based on start and end)
Rule: always print i@(i-1) while moving from start to end
"""
s = int(input())
e = int(input())

out = []
step = 1 if s < e else -1

i = s
while True:
    out.append(f"{i}@{i-1}")
    if i == e:
        break
    i += step

print(", ".join(out))
