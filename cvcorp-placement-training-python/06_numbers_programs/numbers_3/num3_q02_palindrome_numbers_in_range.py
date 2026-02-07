"""
📌 Question 2:
Write a program to print All Palindrome Numbers Between the Given Numbers?

Constraints:
Input  :- First Line of Input Consists of One Integer Value.
          Second Line of Input Consists of One Integer Value.

Output :- Print All Palindrome Numbers Between the Given Numbers.

Constraints:
- Either of the Given Inputs is equal to Zero then Print Invalid Inputs.
- If there is no Palindrome values between the Given Numbers then Print No Palindrome Values.
- If Either of the Given Inputs is Negative then convert those Negative Values to Positive Values.

Example:
Input 1:
100
200
Output:
101 111 121 131 141 151 161 171 181 191
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

    found = False

    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            print(num, end=" ")
            found = True

    if not found:
        print("No Palindrome Values")
