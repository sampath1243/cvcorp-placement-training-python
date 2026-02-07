"""
📌 Question 3: Count Digits in a Number

Write a Program to Count Number of Digits in a Given Number.

Constraints:
- If Input is 0, Print InvaliD Input.
- If Input is Negative, Count Digits and Print that it is Negative Value.

Input:
First Line of Input Consists of One Integer Value.

Output:
Print total number of digits.

Example 1:
Input:
456
Output:
Given Number consists of 3 Digits.

Example 2:
Input:
-1234
Output:
Given Number consists of 4 Digits and it is Negative Value.

Example 3:
Input:
0
Output:
InvaliD Input
"""

# ✅ Answer Code

n = int(input())

if n == 0:
    print("InvaliD Input")
else:
    temp = abs(n)
    count = 0

    while temp > 0:
        count += 1
        temp //= 10

    if n < 0:
        print(f"Given Number consists of {count} Digits and it is Negative Value.")
    else:
        print(f"Given Number consists of {count} Digits.")
