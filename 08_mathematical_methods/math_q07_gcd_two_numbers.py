"""
Question 7:
Write a program to print the GCD of given two numbers.

Constraints:
If both invalid -> "Invalid Inputs"
If n1 invalid -> "Invalid First Input"
If n2 invalid -> "Invalid Second Input."
"""

n1 = int(input())
n2 = int(input())

if n1 <= 0 and n2 <= 0:
    print("Invalid Inputs")
elif n1 <= 0:
    print("Invalid First Input")
elif n2 <= 0:
    print("Invalid Second Input.")
else:
    s = min(n1, n2)
    for i in range(s, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            print(i)
            break
