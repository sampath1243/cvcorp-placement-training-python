'''
Description:
Write a program to find index of an element in a list.

Input :

            First line of input consists of a group of elements for list.

            Second line of input consists an element.

Output :

              Print indexes of the element.


Constraints:
If element was not in the list then print "No Element Found".


Example:
Input 1 : 10 14 12 5 30 34

                5

Output 1 : 3

 

Input 2 : 7 5 8 2 5 4 25 8 54 8 15

               8

Output 2 : 2 7 9
'''


l = list(map(str,input().split()))
k = input()
if k in l:
    c=0
    while k in l:
        print(l.index(k)+c,end=" ")
        l.remove(k)
        c+=1
else:
    print("No Element Found")