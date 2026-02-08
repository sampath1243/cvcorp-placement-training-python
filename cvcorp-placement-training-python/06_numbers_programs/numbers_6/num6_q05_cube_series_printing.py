"""
📌 Numbers - 6 | Question 5
Write a Program to Print the numbers in the following format:
n^3, (n-1)^3, ... , 64, 27, 8, 1.

Constraints:
- If input == 0 print "Invalid Input."
- If input is negative convert to positive

Example:
Input: 9
Output: 729, 512, 343, 216, 125, 64, 27, 8, 1.
"""

n=int(input())

if n==0:
    print("Invalid Input.")
else:
    if n<0:
        n=-n
    c=0
    while n>0:
        s=n**3
        n=n-1
        c+=1
        if c>1:
            print(", ",end="")
        print(s,end="")
    print(".")
