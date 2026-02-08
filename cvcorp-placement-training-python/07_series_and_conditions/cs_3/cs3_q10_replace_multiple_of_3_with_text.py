"""
📌 C & S - 3
Question 10:
Write a program:
Print numbers from 1 to n
If number divisible by 3 print "factor of three"

Separated by ", "
"""

n = int(input())

out = []
for i in range(1, n + 1):
    if i % 3 == 0:
        out.append("factor of three")
    else:
        out.append(str(i))

print(", ".join(out))
