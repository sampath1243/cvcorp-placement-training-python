"""
📌 Numbers - 4
Question 6:
Write a program to check Whether the Given Number(any number of digits) is Armstrong or Not?

Constraints:
- Input must be greater than 0
- Else print "Invalid Input"

Output:
- If Armstrong -> "<n> is a Armstrong Number."
- Else -> "<n> is Not a Armstrong Number."

Example:
Input:
370
Output:
370 is a Armstrong Number.
"""

# ✅ Answer Code

n = int(input())

dc = 0
s = 0

if n <= 0:
    print("Invalid Input")
else:
    t = n
    while t > 0:
        dc += 1
        t //= 10

    t = n
    while t > 0:
        r = t % 10
        s += r ** dc
        t //= 10

    if s == n:
        print(n, "is a Armstrong Number.")
    else:
        print(n, "is Not a Armstrong Number.")
