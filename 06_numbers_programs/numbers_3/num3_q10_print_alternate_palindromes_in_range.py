"""
📌 Numbers - 3 (Updated)
Question 10:
Write a program to print Alternative Palindrome Numbers between the Given Range?

Constraints:
- If any input is negative print "InvAlid InPUts"
- If start > end swap
- If no palindrome values print "No Palindrome Values"
- Range is exclusive
- Print alternate palindrome numbers with comma format ending with dot.

Example:
Input:
100
200
Output:
101, 121, 141, 161, 181.
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
    print("InvAlid InPUts")
else:
    if s > e:
        s, e = e, s

    pals = []
    for i in range(s + 1, e):
        if i > 0 and is_pal(i):
            pals.append(i)

    if len(pals) == 0:
        print("No Palindrome Values")
    else:
        alt = pals[0::2]
        print(", ".join(str(x) for x in alt) + ".")
