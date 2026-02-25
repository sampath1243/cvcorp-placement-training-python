"""
Numbers - 1
Q1: Print First N Prime Numbers

Input: n
Constraint: n > 0 else Invalid Input

Example (n=5):
2 3 5 7 11
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    count = 0
    num = 2

    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")
            count += 1

        num += 1
