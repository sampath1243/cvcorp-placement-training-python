"""
📌 Numbers - 4
Question 2:
Write a program to Count the Number of digits in a Given Number?

Constraints:
- Input must be greater than 10
- Else print "Invalid Input"

Input:
One integer number

Output:
Print count of digits

Example 1:
Input:
4567
Output:
4

Example 2:
Input:
9
Output:
Invalid Input
"""

# ✅ Answer Code

n = int(input())

if n > 10:
    c = 0
    while n > 0:
        c += 1
        n //= 10
    print(c)
else:
    print("Invalid Input")
