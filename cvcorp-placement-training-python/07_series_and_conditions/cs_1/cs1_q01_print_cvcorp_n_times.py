"""
Q1: Print "CVCORP" for N times
Constraint: 10 < N < 100 else print "Invalid Input"
"""
n = int(input())

if 10 < n < 100:
    for _ in range(n):
        print("CVCORP")
else:
    print("Invalid Input")
