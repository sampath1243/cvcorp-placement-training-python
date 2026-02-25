"""
Question 6:
Write a program to print the GCD of given three numbers.

Constraints:
If 2 or 3 inputs are invalid -> "Invalid Inputs"
If n1 invalid -> "Invalid First Input"
If n2 invalid -> "Invalid Second Input"
If n3 invalid -> "Invalid Third Input"
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

c = 0

if n1 <= 0:
    c += 1
if n2 <= 0:
    c += 1
if n3 <= 0:
    c += 1

if c >= 2:
    print("Invalid Inputs")
elif n1 <= 0:
    print("Invalid First Input")
elif n2 <= 0:
    print("Invalid Second Input")
elif n3 <= 0:
    print("Invalid Third Input")
else:
    l = min(n1, n2, n3)
    for i in range(l, 0, -1):
        if n1 % i == 0 and n2 % i == 0 and n3 % i == 0:
            print(i)
            break
