"""
📌 Numbers - 4
Question 9:
Write a program to print the Alternative Armstrong Numbers between the Given Values?

Constraints:
- If any input is 0 print "Invalid Inputs"
- If any input is negative convert to positive
- If no armstrong numbers print "No Armstrong Numbers Between Given Values."
- Range is exclusive
- Print alternate armstrong numbers (1st, 3rd, 5th...)

Output Format:
Alternative Armstrong Numbers between the Given Values is 2, 4, 6, ...

Example:
Input:
1
200
Output:
Alternative Armstrong Numbers between the Given Values is 2, 4, 6, 8, 153.
"""

# ✅ Answer Code

n = int(input())
n1 = int(input())

count = 0
alt_count = 0

if n == 0 or n1 == 0:
    print("Invalid Inputs")
else:
    if n < 0:
        n = -n
    if n1 < 0:
        n1 = -n1

    if n > n1:
        n, n1 = n1, n

    for i in range(n + 1, n1):
        t = i
        c = 0
        sm = 0

        while t > 0:
            c += 1
            t //= 10

        t = i
        while t > 0:
            r = t % 10
            sm += r ** c
            t //= 10

        if sm == i:
            count += 1
            if count % 2 == 1:
                alt_count += 1
                if alt_count == 1:
                    print("Alternative Armstrong Numbers between the Given Values is ", end="")
                else:
                    print(end=", ")
                print(i, end="")

    if alt_count > 0:
        print(".")
    else:
        print("No Armstrong Numbers Between Given Values.")
