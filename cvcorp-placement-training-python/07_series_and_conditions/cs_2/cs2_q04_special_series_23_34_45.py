"""
Q4: Print series like 2*3, 3*4, 4*5, ... , 16*17
Input: start, end
Output 1: pattern
Output 2: multiplied values
"""
s = int(input())
e = int(input())

# Pattern line
parts = []
vals = []
for i in range(s, e):
    parts.append(f"{i}*{i+1}")
    vals.append(str(i * (i + 1)))

print(", ".join(parts))
print(", ".join(vals))
