"""
📌 Numbers - 5
Question 3:
Write a program to Print Sum of First N terms of Fibonacci Series?

Constraints:
- Input must be greater than 0 else print "Invalid Input"

Input:
One integer value (n)

Output:
Print sum of fibonacci series

Example:
Input:
5
Output:
7
(0 + 1 + 1 + 2 + 3 = 7)
"""

# ✅ Answer Code

n=int(input())
s=0

if n>0:
    f1=0
    f2=1
    for i in range(1,n+1):
        s+=f1
        f3=f1+f2
        f1=f2
        f2=f3
    print(s)
else:
    print("Invalid Input")
