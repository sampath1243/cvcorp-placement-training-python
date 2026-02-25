'''
Description:
Write a programto print average of all odd numbers in the given list.

Input :

            Input consists of a group of elements for list.

Output :

            Print average of all odd numbers in the list.


Constraints:
If no odd numbers found in the list then print "No Odd Numbers"


Example:
Input 1 : 18 15 7 93 11 6 31 9

Output 1 : 27.67

Input 2 : 2 84 628 364 128 92 480

Output 2 : No Odd Numbers


'''

l=list(map(int,input().split()))
s=c=0
for i in l:
    if i%2==1:
        s+=i
        c+=1
if c==0:
    print("No Odd Numbers")
else:
    print(f"{s/c:.2f}")

    