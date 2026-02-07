"""
📌 Question 3:
Write a program to print Sum of all Alternative Palindrome Numbers Between the Given Numbers?

Constraints:
Input  :- First Line of Input Consists of One Integer Value.
          Second Line of Input Consists of One Integer Value.

Output :- Print the Sum of All Alternative Palindromes Between the Given Numbers.

Constraints:
- Either of the Given Inputs is equal to Zero then Print Invalid Inputs.
- If there is no Palindrome values between the Given Numbers then Print No Palindrome Values.
- If Either of the Given Inputs is Negative then convert those Negative Values to Positive Values.

Example:
Input:
100
200
Output:
Sum of Alternative Palindrome Numbers between the 100 and 200 is 101 + 121 + 141 + 161 + 181 = 705.
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

    palindromes = []

    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            palindromes.append(num)

    if len(palindromes) == 0:
        print("No Palindrome Values")
    else:
        alt = palindromes[::2]  # 1st, 3rd, 5th...

        expr = " + ".join(map(str, alt))
        total = sum(alt)

        print(f"Sum of Alternative Palindrome Numbers between the {start} and {end} is {expr} = {total}.")
