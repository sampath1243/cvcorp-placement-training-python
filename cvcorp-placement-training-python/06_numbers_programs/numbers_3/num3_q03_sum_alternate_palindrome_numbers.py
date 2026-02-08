"""
📌 Numbers - 3 (Updated)
Question 3:
Write a program to print the Sum of all Alternative Palindrome Numbers Between the Given Numbers?

Constraints:
- Either of the given inputs is equal to zero then print "Invalid Inputs"
- If there is no palindrome values between the given numbers then print "No Palindrome Values"
- If either of the given inputs is negative then convert to positive values
- Range is exclusive
- Output must be in expression format

Output Format:
Sum of Alternative Palindrome Numbers between the <start> and <end> is 101 + 121 + 141 = 363.

Example:
Input:
100
200
Output:
Sum of Alternative Palindrome Numbers between the 100 and 200 is 101 + 121 + 141 + 161 + 181 = 705.
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
    print("Invalid Inputs")
else:
    s = abs(s)
    e = abs(e)

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
        expr = " + ".join(str(x) for x in alt)
        total = sum(alt)

        print(f"Sum of Alternative Palindrome Numbers between the {s} and {e} is {expr} = {total}.")
