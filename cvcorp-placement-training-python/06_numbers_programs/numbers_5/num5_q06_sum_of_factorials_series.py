"""
📌 Numbers - 5
Question 6:
Write a Program to Print Sum of Factorials up to the Given Value?

Constraints:
- If input is negative print "INvalid INput"

Input:
One integer value (n)

Output:
Print factorial series sum in format:
1+1+2+6+24=34

Example:
Input:
4
Output:
1+1+2+6+24=34
"""

# ✅ Answer Code

n=int(input())

if n>=0:
    total_sum=0
    count=0

    for i in range(n+1):
        fact=1
        for j in range(1,i+1):
            fact*=j

        total_sum=total_sum+fact

        if count>0:
            print(end="+")
        print(fact,end="")
        count+=1

    print("="+str(total_sum))
else:
    print("INvalid INput")
