"""
📌 Numbers - 3 (Updated)
Question 9:
Write a program to check whether the given number is Perfect Square or Not?

Constraints:
- If input is negative convert to positive
- If input is 0 print "Invalid Input"

Output:
Given Number is Perfect Square.
OR
Given Number is Not a Perfect Square.

Example:
Input:
25
Output:
Given Number is Perfect Square.
"""

# ✅ Answer Code

n = int(input())

if n == 0:
    print("Invalid Input")
else:
    n = abs(n)
    root = int(n ** 0.5)

    if root * root == n:
        print("Given Number is Perfect Square.")
    else:
        print("Given Number is Not a Perfect Square.")
