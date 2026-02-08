"""
Q7: Print series: 5, 10, 5, 10, ... total N terms
Constraint: N > 0 else "Invalid Input"
"""
n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    out = []
    for i in range(n):
        out.append("5" if i % 2 == 0 else "10")
    print(", ".join(out))
