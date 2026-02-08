"""
📌 Numbers - 3 (Updated)
Question 7:
Write a program to Print Average of Palindrome Numbers between the Given Range?

Constraints:
- If any input is 0 then print "INVALID Inputs"
- If any input is negative convert to positive
- If start > end then print "Given Inputs are Swapped" and swap
- If no palindrome values then print "No Palindrome Values"
- Range is exclusive
- Print average with 2 decimal points

Example:
Input:
100
200
Output:
Given Inputs are Swapped
146.00
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

if s == 0 or e == 0:
    print("INVALID Inputs")
else:
    s = abs(s)
    e = abs(e)

    if s > e:
        print("Given Inputs are Swapped")
        s, e = e, s

    total = 0
    count = 0

    for i in range(s + 1, e):
        if i > 0 and is_pal(i):
            total += i
            count += 1

    if count == 0:
        print("No Palindrome Values")
    else:
        avg = total / count
        print(f"{avg:.2f}")
