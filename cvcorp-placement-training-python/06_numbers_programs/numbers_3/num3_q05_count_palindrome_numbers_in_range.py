"""
📌 Question 5:
Write a program to Count Number of Palindrome Values Between the Given Numbers?

Constraints:
Input  :- First Line of Input Consists of One Integer Value.
          Second Line of Input Consists of One Integer Value.

Output :- Print the Count of Palindrome Values.

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

    count = 0

    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            count += 1

    if count == 0:
        print("No Palindrome Values")
    else:
        print(count)
