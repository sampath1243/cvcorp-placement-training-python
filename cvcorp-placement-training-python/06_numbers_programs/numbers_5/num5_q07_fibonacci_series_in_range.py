"""
📌 Numbers - 5
Question 7:
Write a program to Print Fibonacci Series in the Given Range?

Constraints:
- Both inputs must be >= 0 else print "Invalid Inputs"
- If first input > second input swap
- If no fibonacci values in range print "No Fibonacci Series Values"

Input:
First Line  : Start value
Second Line : End value

Output:
Print fibonacci values in range

Example:
Input:
10
50
Output:
13 21 34
"""

# ✅ Answer Code

n=int(input())
n1=int(input())

if n>n1:
    n,n1=n1,n

if n>=0 and n1>=0:
    f1=0
    c=0
    f2=1

    for i in range(1,n1+1):
        if f1>n1:
             break
        if f1>=n:
            c+=1
            print(f1, end=" ")

        f3=f1+f2
        f1=f2
        f2=f3

    if c==0:
        print("No Fibonacci Series Values")
else:
    print("Invalid Inputs")
