"""
📌 C & S - 3
Question 8:
Write a program:
Print numbers from 1 to n-1
If number is even print "even"
Else print the number

Separated by ", "
"""

n = int(input())

out = []
for i in range(1, n):
    if i % 2 == 0:
        out.append("even")
    else:
        out.append(str(i))

print(", ".join(out))
