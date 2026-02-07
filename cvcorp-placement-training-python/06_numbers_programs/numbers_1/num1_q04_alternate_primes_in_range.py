"""
Numbers - 1
Q4: Alternate Prime Numbers in Range

Input: start end
Rules:
- if start > end -> Invalid Range
- if start < 0 or end < 0 -> Invalid Input

Example:
Input: 10 40
Output: 11 17 23 31 37
"""

start, end = map(int, input().split())

if start < 0 or end < 0:
    print("Invalid Input")
elif start > end:
    print("Invalid Range")
else:
    prime_count = 0
    found = False

    for num in range(start, end + 1):
        if num > 1:
            prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime = False
                    break

            if prime:
                prime_count += 1
                if prime_count % 2 == 1:  # print 1st, 3rd, 5th primes...
                    print(num, end=" ")
                    found = True

    if not found:
        print("No Numbers")
