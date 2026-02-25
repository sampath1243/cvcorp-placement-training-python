"""
📌 Question 7: Sum of Even Digits in a Number

Write a Program to Find Sum of Even Digits in a Given Number.

Constraints:
- Given Input Must be Greater than Zero, else Print Invalid Input.

Input:
First Line of Input Consists of One Integer Value.

Output:
Print sum of even digits.

Example:
Input:
2568
Output:
16
(2 + 6 + 8 = 16)
"""

# ✅ Answer Code

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    total = 0
    temp = n

    while temp > 0:
        d = temp % 10
        if d % 2 == 0:
            total += d
        temp //= 10

    print(total)
