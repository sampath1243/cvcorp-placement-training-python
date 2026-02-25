"""
Question 2:
Write a program to print the LCM of given three numbers.

Constraints:
'n1' Value is Must be Greater than zero or else Print "InvalId First Input".
'n2' Value is Must be Greater than zero or else Print "Invalid Second Input".
'n3' Value is Must be Greater than zero or else Print "InvaliD ThirD Input".
If any of two or three values <= 0 print "Sorry Invalid Inputs!"
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

h = max(n1, n2, n3)
m = h

if n1 > 0 and n2 > 0 and n3 > 0:
    while True:
        if h % n1 == 0 and h % n2 == 0 and h % n3 == 0:
            print(h)
            break
        h = h + m
elif n1 <= 0 and n2 > 0 and n3 > 0:
    print("InvalId First Input")
elif n2 <= 0 and n1 > 0 and n3 > 0:
    print("Invalid Second Input")
elif n3 <= 0 and n2 > 0 and n1 > 0:
    print("InvaliD ThirD Input")
else:
    print("Sorry Invalid Inputs!")
