"""
Q10:
If n not in 100..1000 -> "WRONG NUMBER"
Else:
- If even: remainder when divided by 3
- If odd : remainder when divided by 2
"""
n = int(input())

if n < 100 or n > 1000:
    print("WRONG NUMBER")
else:
    if n % 2 == 0:
        print(n % 3)
    else:
        print(n % 2)
