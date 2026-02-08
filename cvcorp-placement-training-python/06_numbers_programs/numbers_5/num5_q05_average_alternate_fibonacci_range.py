"""
📌 Numbers - 5
Question 5:
Write a program to Print Average of Alternative Fibonacci Series between the Given Range?

Constraints:
- Both inputs must be >= 0 else print "Invalid Inputs"
- If first input > second input swap
- If no fibonacci values in range print "No Fibonacci Series Values"

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
6.00
"""

# ✅ Answer Code

n1=int(input())
n2=int(input())

c=0
s=0
count=0

if n1>n2:
        n1,n2=n2,n1

if n1>=0 and n2>=0:

    f1=0
    f2=1
    for i in range(1,n2+1):
        if f1>=n2:
            break
        if f1>=n1:
            c+=1
            if c%2==1:
                count+=1
                s+=f1

        f3=f1+f2
        f1=f2
        f2=f3

    if c==0:
        print("No Fibonacci Series Values")
    else:
        print("%.2f" %(s/count))
else:
    print("Invalid Inputs")
