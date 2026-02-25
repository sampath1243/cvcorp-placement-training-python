"""
Question 1:
Write a program to print the LCM of given two numbers.

Constraints:
Both the values 'n1' & 'n2' must be Greater than zero or else Print "Invalid Inputs.".
'n1' Value is Must be Greater than zero or else Print "Invalid First Input".
'n2' Value is Must be Greater than zero or else Print "InValid Second Input".
"""

n1 = int(input())
n2 = int(input())

h = max(n1, n2)
m = h

if n1 > 0 and n2 > 0:
    while True:
        if h % n1 == 0 and h % n2 == 0:
            print(h)
            break
        h += m
elif n1 <= 0 and n2 > 0:
    print("Invalid First Input")
elif n2 <= 0 and n1 > 0:
    print("InValid Second Input")
else:
    print("Invalid Inputs.")
