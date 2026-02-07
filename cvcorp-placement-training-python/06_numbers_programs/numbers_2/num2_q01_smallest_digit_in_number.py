"""
📌 Question 1: Smallest Digit in a Number

Write a Program to Print the Smallest Digit in a Given Number.

Constraints:
- Given Input Must be Greater than Zero, else Print Invalid Input.

Input:
First Line of Input Consists of One Integer Value.

Output:
Print the Smallest Digit in the Given Number.

Example 1:
Input:
85254
Output:
Smallest Digit in a Given Number is 2.

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
    smallest = 9
    temp = n

    while temp > 0:
        d = temp % 10
        if d < smallest:
            smallest = d
        temp //= 10

    print(f"Smallest Digit in a Given Number is {smallest}.")
