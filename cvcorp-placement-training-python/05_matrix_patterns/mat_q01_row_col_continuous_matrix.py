"""
Matrix Patterns
Q1: Row x Col Continuous Matrix

Input: r c
Constraint: r>0 and c>0 else Invalid Input

Example:
Input:
3
4

Output:
1 2 3 4
5 6 7 8
9 10 11 12
"""

r = int(input())
c = int(input())

if r <= 0 or c <= 0:
    print("Invalid Input")
else:
    num = 1
    for i in range(r):
        for j in range(c):
            print(num, end=" ")
            num += 1
        print()
