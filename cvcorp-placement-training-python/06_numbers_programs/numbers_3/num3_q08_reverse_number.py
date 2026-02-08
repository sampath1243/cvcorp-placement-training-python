"""
📌 Numbers - 3 (Updated)
Question 8:
Write a program to print Reverse of a Given Number?

Constraints:
- If input is less than or equal to 0 then print "InValid Input"

Example:
Input:
1234
Output:
4321
"""

# ✅ Answer Code

n = int(input())

if n <= 0:
    print("InValid Input")
else:
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10

    print(rev)
