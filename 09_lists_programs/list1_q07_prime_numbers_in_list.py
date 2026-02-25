'''
Description:
Write a program to print prime numbers in the given list.

Input :

            Input consists of a group of elements for list.

Output :

            Print all prime numbers in the list.


Constraints:
If no prime numbers found in the list then print "No Prime Numbers"


Example:
Input 1 : 18 15 7 93 11 6 31 9

Output 1 : 7 11 31

 

Input 2 : 21 6 90 26 252 16 75

Output 2 : No Prime Numbers '''

def isPrime(n):
    i=-1
    for i in range(2,n):
        if n%i==0:
            break;
    if i==n-1 or n==2:
        return True
    return False
l=list(map(int,input().split()))
b=False
for i in l:
    if isPrime(i):
        print(i,end=" ")
        b=True
if not b :
    print("No Prime Numbers")