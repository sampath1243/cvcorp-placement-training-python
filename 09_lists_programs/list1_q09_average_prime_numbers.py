'''
Description:
Write a program to print average of all prime numbers in the given list.

Input :

            Input consists of a group of elements for list.

Output :

            Print average of all prime numbers in the list.


Constraints:
If no prime numbers found in the list then print "No Prime Numbers"


Example:
Input 1 : 18 15 7 93 11 6 31 9

Output 1 : The average of all prime numbers in the given list is 16.33

Input 2 : 21 6 90 26 252 16 75

Output 2 : No Prime Numbers 
'''

def isPrime(n):
    i=-1
    for i in range(2,n):
        if n%i==0:
            break;
    if i==n-1 or n==2:
        return True
    return False
l=list(map(int,input().split()))
s=c=0
for i in l:
    if isPrime(i):
        s+=i
        c+=1
if s==0:
    print("No Prime Numbers")
else:
    print(f"The average of all prime numbers in the given list is {s/c:.2f}")