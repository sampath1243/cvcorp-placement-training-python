"""
📌 Numbers - 5
Question 2:
Write a program to Print Average of Fibonacci Series between the Given Range?

Constraints:
- Both inputs must be greater than or equal to 0 else print "Invalid Inputs"
- If no fibonacci values in range print "No Fibonacci Series Values"
- If first input > second input swap

Input:
First Line  : Start value
Second Line : End value

Output:
Print average value in 2 decimal format

Example:
Input:
1
20
Output:
7.00
"""

# ✅ Answer Code

n1=int(input())
n2=int(input())

sum=0
c=0

if n1>=0 and n2>=0:

    f1=0
    f2=1

    if n1>n2:
        n1,n2=n2,n1

    for i in range(1,n2+1):
        if f1>n2:
             break

        if f1>=n1 and f1<=n2:
            c+=1
            sum+=f1

        f3=f1+f2
        f1=f2
        f2=f3

    if c>0:
        print("%.2f" %(sum/c))
    else:
        print("No Fibonacci Series Values")
else:
    print("Invalid Inputs")
