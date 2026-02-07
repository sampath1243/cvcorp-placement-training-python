"""
Numbers - 1
Q2: Print Prime Numbers in a Range

Input: start end
Rules:
- if start > end -> Invalid Range
- if start < 0 or end < 0 -> Invalid Input

Example:
Input: 10 30
Output: 11 13 17 19 23 29
"""

start, end = map(int, input().split())

if start < 0 or end < 0:
    print("Invalid Input")
elif start > end:
    print("Invalid Range")
else:
    found = False
    for num in range(start, end + 1):
        if num > 1:
            prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                print(num, end=" ")
                found = True

    if not found:
        print("No Numbers")
