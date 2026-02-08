"""
📌 Numbers - 3 (Updated)
Question 6:
Write a Program to check whether the given number is Palindrome or Not.
If Palindrome print:
"Given Number is Palindrome"
Else print:
"Reverse of a Given Number is <reverse>"

Constraints:
- If input < 0 then print "Invalid Input"
- If input == 0 then print "Zero"

Example 1:
Input:
121
Output:
Given Number is Palindrome

Example 2:
Input:
123
Output:
Reverse of a Given Number is 321
"""

# ✅ Answer Code

n = int(input())

if n < 0:
    print("Invalid Input")
elif n == 0:
    print("Zero")
else:
    original = n
    rev = 0

    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10

    if rev == original:
        print("Given Number is Palindrome")
    else:
        print("Reverse of a Given Number is", rev)

