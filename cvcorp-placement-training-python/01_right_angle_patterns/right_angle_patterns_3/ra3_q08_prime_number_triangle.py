"""
Right Angle Patterns - 3
Q8: Prime Number Triangle (prefix primes each row)

Input: n
Rules:
- if n==0 -> "Invalid Input"
- if n<0 -> convert to positive

Example (n=5):
2
2 3
2 3 5
2 3 5 7
2 3 5 7 11
"""

n = int(input())

if n == 0:
    print("Invalid Input")
else:
    if n < 0:
        n = -n

    primes = []
    x = 2

    while len(primes) < n:
        is_prime = True
        for p in range(2, int(x ** 0.5) + 1):
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
        x += 1

    for i in range(1, n + 1):
        for j in range(i):
            print(primes[j], end=" ")
        print()
