'''Description:
Write a program to take two list inputs from the user then merge two lists into one list then print that merged list.

 

Input : First line of input consists a group of elements for first list.

            Second line of input consists a group of elements for second list.

 

Output : Print merged list.


Constraints:
NA


Example:
Input : 10 14 5 12 30 34

             2 8 4 3 2 15

Output : 10 14 5 12 30 34 2 8 4 3 2 15


'''

l1 = list(map(str,input().split()))
l2 = list(map(str,input().split()))
l1.extend(l2)
for i in l1:
    print(i,end=" ")