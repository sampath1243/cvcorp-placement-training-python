"""
📌 Numbers - 4
Question 8:
Write a program to print the Armstrong Numbers between the Given two values.

Constraints:
- If any input is 0 print "Invalid Inputs"
- If any input is negative convert to positive
- If no armstrong numbers print "No Armstrong Numbers Between Given Values"
- Range is exclusive (between only)

Output Format:
Armstrong Numbers between the Given Values is 2, 3, ... .

Example:
Input:
1
200
Output:
Armstrong Numbers between the Given Values is 2, 3, 4, 5, 6, 7, 8, 9, 153.
"""

# ✅ Answer Code

s = int(input())
e = int(input())

count = 0

if s == 0 or e == 0:
    print("Invalid Inputs")
else:
    if s < 0:
        s = -s
    if e < 0:
        e = -e

    if s > e:
        s, e = e, s

    for i in range(s + 1, e):
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
            if count == 1:
                print("Armstrong Numbers between the Given Values is ", end="")
            if count > 1:
                print(end=", ")
            print(i, end="")

    if count > 0:
        print(".")
    else:
        print("No Armstrong Numbers Between Given Values")
