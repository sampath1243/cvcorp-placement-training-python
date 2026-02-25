"""
📌 Numbers - 4
Question 3:
Write a program to swap the two given numbers (without using a third variable).

Input:
First number
Second number

Output:
Print swapped values each on new line

Example:
Input:
10
20
Output:
20
10
"""

# ✅ Answer Code

n = int(input())
n1 = int(input())

n, n1 = n1, n
print(n)
print(n1)

