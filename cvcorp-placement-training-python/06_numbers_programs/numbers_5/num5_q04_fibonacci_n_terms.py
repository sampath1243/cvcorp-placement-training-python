"""
📌 Numbers - 5
Question 4:
Write a program to Print First N terms of Fibonacci Series?

Constraints:
- If input is equal to zero print "Invalid Input"
- If input is negative convert to positive

Input:
One integer value (n)

Output:
Print fibonacci series values

Example 1:
Input:
5
Output:
0 1 1 2 3

Example 2:
Input:
0
Output:
Invalid Input
"""

# ✅ Answer Code

n=int(input())

if n==0:
    print("Invalid Input")
else:
    if n<0:
        n=-n
    f1=0
    f2=1
    for i in range(1,n+1):
        print(f1,end=" ")
        f3=f1+f2
        f1=f2
        f2=f3
