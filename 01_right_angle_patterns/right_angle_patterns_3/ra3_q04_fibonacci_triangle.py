"""
Right Angle Patterns - 3
Q4: Fibonacci Triangle (Prefix Fibonacci each row)

Input: n
Rules:
- if n==0 -> "Invalid Input"
- if n<0 -> convert to positive

Example (n=6):
1
1 2
1 2 3
1 2 3 5
1 2 3 5 8
1 2 3 5 8 13
"""

n = int(input())

if n == 0:
    print("Invalid Input")
else:
    if n < 0:
        n = -n

    fib = []
    a, b = 1, 2
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    for i in range(1, n + 1):
        for j in range(i):
            print(fib[j], end=" ")
        print()
