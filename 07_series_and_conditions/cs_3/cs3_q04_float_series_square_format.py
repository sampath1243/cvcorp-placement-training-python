"""
Q4: Print: s^2, (s+0.2)^2, ... , e^2
Separated by ", " and end with "."
Example: 10.7^2, 10.9^2, ... , 12.1^2.
"""
s = float(input())
e = float(input())

out = []
x = s
while round(x, 1) <= e:
    out.append(f"{x:.1f}^2")
    x = round(x + 0.2, 1)

print(", ".join(out) + ".")
