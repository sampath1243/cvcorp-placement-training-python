"""
Description:
Write a program to count the element number of times occurred in list.

Input :

            First line of input consists of a group of elements for list.

Output :

            Second line of input consists of an element.


Constraints:
If element was not in the list then print "No Element Found".


Example:
Input : 5 7 54 1 5 8 7 54 7 2 3

            7

Output : 3


Explanation:
NA
"""

l = list(map(str,input().split()))
k = input()
c=0
if k in l:
    for i in l:
        if i==k:
            c+=1
    print(c)
else:
    print("No Element Found")