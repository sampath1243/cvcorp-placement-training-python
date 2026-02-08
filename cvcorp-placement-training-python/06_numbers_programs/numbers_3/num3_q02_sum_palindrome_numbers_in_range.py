"""
📌 Numbers - 3 (Updated)
Question 2:
Write a program to print the Sum of all Palindrome Numbers Between the Given Numbers?

Constraints:
- Either of the given inputs is equal to zero then print "INVALID Inputs"
- If there is no palindrome values between the given numbers then print "No Palindrome Values"
- If either of the given inputs is negative then convert those negative values to positive values
- Range is exclusive (between values only)

Input:
First Line : start value
Second Line: end value

Output:
Print the sum of palindrome numbers between the range

Example 1:
Input:
100
200
Output:
1460

Example 2:
Input:
-20
25
Output:
22
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
        s, e = e, s

    total = 0
    found = False

    for i in range(s + 1, e):
        if i > 0 and is_pal(i):
            total += i
            found = True

    if found:
        print(total)
    else:
        print("No Palindrome Values")
