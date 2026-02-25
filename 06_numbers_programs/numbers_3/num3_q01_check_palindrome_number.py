"""
📌 Numbers - 3 (Updated)
Question 1:
Write a program to check whether the given number is Palindrome or Not?

Constraints:
- If input is less than or equal to 0 then print "InvAlid Input"

Input:
First Line of Input Consists of One Integer Value.

Output:
Print "Palindrome" if number is palindrome else print "Not a Palindrome"

Example 1:
Input:
121
Output:
Palindrome

Example 2:
Input:
123
Output:
Not a Palindrome

Example 3:
Input:
0
Output:
InvAlid Input
"""

# ✅ Answer Code

n = int(input())

if n <= 0:
    print("InvAlid Input")
else:
    original = n
    rev = 0

    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10

    if rev == original:
        print("Palindrome")
    else:
        print("Not a Palindrome")
