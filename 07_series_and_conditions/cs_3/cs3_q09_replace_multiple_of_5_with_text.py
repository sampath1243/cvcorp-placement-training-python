"""
📌 C & S - 3
Question 9:
Write a program:
Print odd numbers from 1 to n
If odd number divisible by 5 print "divisible by five"

Separated by ", "
"""

n = int(input())

out = []
for i in range(1, n + 1):
    if i % 2 == 1:
        if i % 5 == 0:
            out.append("divisible by five")
        else:
            out.append(str(i))

print(", ".join(out))
