'''Description:
Write a program to take inputs from the user and print the list values

Input : Group of integers seperated by space

Output : print the list elements one by one 


Constraints:
NA


Example:
Input 1 : 10 14 5 12 30 34

Output 1 : 10

                 14

                 5

                 12

                 30

                 34'''
l = list(map(int,input().split()))
for i in l:
    print(i)