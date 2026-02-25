"""
📌 Numbers - 5
Question 8:
Write a Program to Print Factorial of a Given Number?

Constraints:
- If input is negative print "Invalid InPut"

Input:
One integer value (n)

Output:
Print factorial value

Example:
Input:
5
Output:
120
"""

# ✅ Answer Code

n=int(input())

if n>=0:
    sum=1
    for i in range(1,n+1):
        sum=sum*i
    print(sum)
else:
    print("Invalid InPut")
