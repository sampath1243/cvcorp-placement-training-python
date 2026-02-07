"""
📌 Question 7:
Write a program to Print Palindrome Numbers Between the Given Range and Print Their Sum Expression?

Constraints:
- Either of the Given Inputs is equal to Zero then Print Invalid Inputs.
- If there is no Palindrome values between the Given Numbers then Print No Palindrome Values.
- If Either of the Given Inputs is Negative then convert those Negative Values to Positive Values.

Example:
Input:
100
200
Output:
sum = 101 + 111 + 121 + ... + 191 = 1460
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

    pals = []

    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            pals.append(num)

    if len(pals) == 0:
        print("No Palindrome Values")
    else:
        expr = " + ".join(map(str, pals))
        total = sum(pals)
        print(f"sum = {expr} = {total}")
