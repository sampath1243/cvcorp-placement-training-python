'''Description:
Write a program to add an element to the list at particular index

Input : first line of input consists of group of integers

           Second line of input consists of a integer which represents element

           Third line of input consists of a integer which represents index

Output :  Print the list after adding the element into the list at given position


Constraints:
If the index is out of the range add at the end of the list


Example:
Input 1 : 10 14 5 12 30 34  
               2  
               99

Output 1: 10

               14

               99

               5

               12

               30

               34

'''

l = list(map(int,input().split()))
idx = int(input())
ele = int(input())
l.insert(idx,ele)
for i in l:
	print(i)