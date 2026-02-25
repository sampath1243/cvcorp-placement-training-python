"""
📌 Numbers - 3 (Updated)
Question 5:
Write a program to print All Palindrome Numbers Between the Given Range?

Constraints:
- If any input is negative then print "InvaliD InputS"
- If start > end swap values
- If no palindrome values then print "No Palindrome Values"
- Range is exclusive
- Print each palindrome in new line

Example:
Input:
100
200
Output:
101
111
121
131
141
151
161
171
181
191
"""

# ✅ Answer Code

s = int(input())
e = int(input())

def is_pal(num):
    temp = num
    rev = 0
    while temp > 0:
        rev = rev * 10 + (temp % 10)
        temp //= 10
    return rev == num

if s < 0 or e < 0:
    print("InvaliD InputS")
else:
    if s > e:
        s, e = e, s

    found = False
    for i in range(s + 1, e):
        if i > 0 and is_pal(i):
            print(i)
            found = True

    if not found:
        print("No Palindrome Values")
