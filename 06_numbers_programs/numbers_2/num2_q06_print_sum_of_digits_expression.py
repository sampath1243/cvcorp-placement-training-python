"""
📌 Question 6: Print Digits as Addition Expression

Write a Program to Print Digits of a Given Number in Addition Format.

Constraints:
- Given Input Must be Greater than Zero, else Print Invalid Input.

Input:
First Line of Input Consists of One Integer Value.

Output:
Print digits in addition format.

Example:
Input:
2568
Output:
2 + 5 + 6 + 8.
"""

# ✅ Answer Code

n = int(input())

if n <= 0:
    print("Invalid Input.")
else:
    digits = list(str(n))
    print(" + ".join(digits) + ".")
