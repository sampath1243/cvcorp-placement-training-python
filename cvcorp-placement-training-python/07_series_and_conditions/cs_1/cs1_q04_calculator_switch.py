"""
Q4: Calculator using operator (+, -, *, //, %)
Input:
a
b
op
If op not one of + - * // % -> print "Invalid Input"
"""
a = int(input())
b = int(input())
op = input().strip()

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "//":
    print(a // b)
elif op == "%":
    print(a % b)
else:
    print("Invalid Input")
