'''
Description:
Write a program to remove an element at particular index in a list.

Input :

             First line of input consists of a group of elements for list.

             Second line of input consists of an integer which represents an index.

Output :

            Print the list after removing the element at given position.


Constraints:
If index is not with in range then print "Invalid Index Input".

Index value might be negative.


Example:
Input 1 : 10 14 5 12 30 34

               2

Output 1 : 10 14 12 30 34

 

Input 2 : 12 16 8 17 6 9 2

              -2

Output 2 : 12 16 8 17 6 2
'''

l1 = list(map(str,input().split()))
k = int(input())
n = len(l1)
m = -n
if(k<n and k>=0) or (k>=m and k<0):
    l1.pop(k)
    for i in l1:
        print(i,end=" ")
else:
    print("Invalid Index Input")