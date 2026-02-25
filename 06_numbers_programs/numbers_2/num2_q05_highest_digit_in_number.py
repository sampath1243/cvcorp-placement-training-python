"""
📌 Question 5: Highest Digit in a Number

Write a Program to Print the Highest Digit in a Given Number.

Constraints:
- Given Input Must be Greater than Zero, else Print Invalid Input.

Input:
First Line of Input Consists of One Integer Value.

Output:
Print the Highest Digit.

Example 1:
Input:
85254
Output:
Highest Digit in a Given Number is 8.

Example 2:
Input:
-6
Output:
Invalid Input.
"""

# ✅ Answer Code

n = int(input())

if n <= 0:
    print("Invalid Input.")
else:
    highest = 0
    temp = n

    while temp > 0:
        d = temp % 10
        if d > highest:
            highest = d
        temp //= 10

    print(f"Highest Digit in a Given Number is {highest}.")
