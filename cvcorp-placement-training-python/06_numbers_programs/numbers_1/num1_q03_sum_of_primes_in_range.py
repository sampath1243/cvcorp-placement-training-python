"""
Numbers - 1
Q3: Sum of Prime Numbers in Range

Input: start end
Rules:
- if start > end -> Invalid Range
- if start < 0 or end < 0 -> Invalid Input

Example:
Input: 10 20
Output: 60
(primes: 11 + 13 + 17 + 19 = 60)
"""

start, end = map(int, input().split())

if start < 0 or end < 0:
    print("Invalid Input")
elif start > end:
    print("Invalid Range")
else:
    total = 0
    for num in range(start, end + 1):
        if num > 1:
            prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                total += num

    print(total)
