"""
📌 Question 6:
Write a program to Print Sum of Digits of All Palindrome Numbers Between the Given Numbers?

Constraints:
- Either of the Given Inputs is equal to Zero then Print Invalid Inputs.
- If there is no Palindrome values between the Given Numbers then Print No Palindrome Values.
- If Either of the Given Inputs is Negative then convert those Negative Values to Positive Values.
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
            total += sum(int(d) for d in str(num))
            found = True

    if found:
        print(total)
    else:
        print("No Palindrome Values")
