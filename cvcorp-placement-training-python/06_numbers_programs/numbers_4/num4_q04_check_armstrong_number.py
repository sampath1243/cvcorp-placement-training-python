"""
📌 Numbers - 4
Question 4:
Write a program to check if the Given Number is Armstrong or not?

Constraints:
- Input must be greater than 0
- Else print "Invalid Input"

Output:
- If Armstrong -> "Armstrong Number"
- Else -> "Not a Armstrong Number"

Example:
Input:
153
Output:
Armstrong Number
"""

# ✅ Answer Code

n = int(input())

count = 0
s = 0

if n <= 0:
    print("Invalid Input")
else:
    t = n
    while t > 0:
        t //= 10
        count += 1

    t = n
    while t > 0:
        r = t % 10
        s += r ** count
        t //= 10

    if s == n:
        print("Armstrong Number")
    else:
        print("Not a Armstrong Number")
