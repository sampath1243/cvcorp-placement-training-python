"""
📌 Question 2: Check Perfect Square

Write a Program to Check whether the Given Number is a Perfect Square or Not.

Constraints:
- Given Input Must be Greater than Zero, else Print InvaliD Input.

Input:
First Line of Input Consists of One Integer Value.

Output:
Print whether it is Perfect Square or Not.

Example 1:
Input:
25
Output:
Given Number is a Perfect Square.

Example 2:
Input:
26
Output:
Given Number is Not a Perfect Square.

Example 3:
Input:
-6
Output:
InvaliD Input
"""

# ✅ Answer Code

n = int(input())

if n <= 0:
    print("InvaliD Input")
else:
    i = 1
    while i * i < n:
        i += 1

    if i * i == n:
        print("Given Number is a Perfect Square.")
    else:
        print("Given Number is Not a Perfect Square.")
