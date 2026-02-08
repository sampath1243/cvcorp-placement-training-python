"""
📌 Numbers - 5
Question 1:
Write a program to Print First N terms of Alternative Fibonacci Series?

Constraints:
- Given input must not be equal to zero else print "Invalid Input"
- If input is negative convert to positive

Input:
First Line of Input Consists of One Integer Value (n)

Output:
Print Alternative Fibonacci Series values

Example 1:
Input:
5
Output:
0, 1, 2, 5, 13

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
    print(f1,end=", ")

    f3=f1+f2
    c=0
    d=0

    while c+3<=(n*2):
        c+=1
        if c%2==1:
            d+=1
            if d>1:
                print(end=", ")
            print(f3,end="")

        f1=f2
        f2=f3
        f3=f1+f2
