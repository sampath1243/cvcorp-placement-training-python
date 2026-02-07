"""
📌 Question 9:
Write a program to Print Sum of Palindrome Numbers Between the Given Values?

Constraints:
- Either of the Given Inputs is equal to Zero then Print Invalid Inputs.
- If there is no Palindrome values between the Given Numbers then Print No Palindrome Values.
- If Either of the Given Inputs is Negative then convert those Negative Values to Positive Values.

Example:
Input:
100
200
Output:
1460
"""

# ✅ Answer Code

a = int(input())
b = int(input())

if a == 0 or b == 0:
    print("Invalid Inputs")
else:
    a = abs(a)
    b = abs(b)

    start = min(a, b)
    end = max(a, b)

    total = 0
    found = False

    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            total += num
            found = True

    if found:
        print(total)
    else:
        print("No Palindrome Values")
