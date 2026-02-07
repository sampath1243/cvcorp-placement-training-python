"""
📌 Question 1:
Write a program to print Sum of all Palindrome Numbers Between the Given Numbers?

Constraints:
Input  :- First Line of Input Consists of One Integer Value.
          Second Line of Input Consists of One Integer Value.

Output :- Print the Sum of All Palindromes Between the Given Numbers.

Constraints:
- Either of the Given Inputs is equal to Zero then Print Invalid Inputs.
- If there is no Palindrome values between the Given Numbers then Print No Palindrome Values.
- If Either of the Given Inputs is Negative then convert those Negative Values to Positive Values.

Example:
Input 1:
100
200
Output 1:
1460

Input 2:
-20
25
Output 2:
22
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
