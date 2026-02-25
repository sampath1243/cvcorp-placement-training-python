'''
Description:
Write a program to remove particular element in a list and print a list after remving.

Input :

            First line of input consists a group of elements for list.

            Second line of input consists one element which represents removing element.

Output : 

            Print the list after removing the particular element.


Constraints:
If removing element not in list print "No element Found".


Example:
Input 1 : 10 14 5 12 30 34

               5

Output 1 : 10 14 12 30 34

 

Input 2 : 10 14 12 14 6 51 14 2

               14

Output 2: 10 12 6 51 2


'''

l1 = list(map(str,input().split()))
k = input()
if k in l1:
    while k in l1:
        l1.remove(k)
    for i in l1:
        print(i,end=" ")
else:
    print("No element Found")