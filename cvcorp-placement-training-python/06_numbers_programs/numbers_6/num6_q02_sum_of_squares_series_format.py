"""
📌 Numbers - 6 | Question 2
Write a Program to Find the result of the following expression:
n^2 + (n-1)^2 + ... + 16 + 9 + 4 + 1 = ?

Constraints:
- If input == 0 print "Invalid Input"
- If input is negative, convert to positive

Example:
Input: 9
Output: 81 + 64 + 49 + 36 + 25 + 16 + 9 + 4 + 1 = 285
Input: 5
Output: 25 + 16 + 9 + 4 + 1 = 55.
"""

n=int(input())

if n==0:
    print("Invalid Input")
else:
    sum=0
    c=0
    if n<=0:
        n=-n

    while n>0:
        s=n**2
        sum=sum+s
        n=n-1
        c+=1
        if c>1:
            print(" + ",end="")
        print(s,end="")
    print(" = "+str(sum))
